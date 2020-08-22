from PyQt5 import QtCore, QtGui, QtWidgets

class NeumorphismEffect(QtWidgets.QGraphicsEffect):
    originChanged = QtCore.pyqtSignal(QtCore.Qt.Corner)
    distanceChanged = QtCore.pyqtSignal(float)
    colorChanged = QtCore.pyqtSignal(QtGui.QColor)
    clipRadiusChanged = QtCore.pyqtSignal(int)

    _cornerShift = (QtCore.Qt.TopLeftCorner, QtCore.Qt.TopRightCorner, 
        QtCore.Qt.BottomRightCorner, QtCore.Qt.BottomLeftCorner)

    def __init__(self, distance=4, color=None, origin=QtCore.Qt.TopLeftCorner, clipRadius=0):
        super().__init__()

        self._leftGradient = QtGui.QLinearGradient(1, 0, 0, 0)
        self._leftGradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        self._topGradient = QtGui.QLinearGradient(0, 1, 0, 0)
        self._topGradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)

        self._rightGradient = QtGui.QLinearGradient(0, 0, 1, 0)
        self._rightGradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        self._bottomGradient = QtGui.QLinearGradient(0, 0, 0, 1)
        self._bottomGradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)

        self._radial = QtGui.QRadialGradient(.5, .5, .5)
        self._radial.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        self._conical = QtGui.QConicalGradient(.5, .5, 0)
        self._conical.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)

        self._origin = origin
        distance = max(0, distance)
        self._clipRadius = min(distance, max(0, clipRadius))
        self._setColor(color or QtWidgets.QApplication.palette().color(QtGui.QPalette.Window))
        self._setDistance(distance)

    def color(self):
        return self._color

    @QtCore.pyqtSlot(QtGui.QColor)
    @QtCore.pyqtSlot(QtCore.Qt.GlobalColor)
    def setColor(self, color):
        if isinstance(color, QtCore.Qt.GlobalColor):
            color = QtGui.QColor(color)
        if color == self._color:
            return
        self._setColor(color)
        self._setDistance(self._distance)
        self.update()
        self.colorChanged.emit(self._color)

    def _setColor(self, color):
        self._color = color
        self._baseStart = color.darker(110)
        self._baseStop = QtGui.QColor(self._baseStart)
        self._baseStop.setAlpha(0)
        self._shadowStart = self._baseStart.darker(125)
        self._shadowStop = QtGui.QColor(self._shadowStart)
        self._shadowStop.setAlpha(0)

        self.lightSideStops = [(0, self._baseStart), (1, self._baseStop)]
        self.shadowSideStops = [(0, self._shadowStart), (1, self._shadowStop)]
        self.cornerStops = [(0, self._shadowStart), (.25, self._shadowStop), 
            (.75, self._shadowStop), (1, self._shadowStart)]

        self._setOrigin(self._origin)

    def distance(self):
        return self._distance

    def setDistance(self, distance):
        if distance == self._distance:
            return
        oldRadius = self._clipRadius
        self._setDistance(distance)
        self.updateBoundingRect()
        self.distanceChanged.emit(self._distance)
        if oldRadius != self._clipRadius:
            self.clipRadiusChanged.emit(self._clipRadius)

    def _getCornerPixmap(self, rect, grad1, grad2=None):
        pm = QtGui.QPixmap(self._distance + self._clipRadius, self._distance + self._clipRadius)
        pm.fill(QtCore.Qt.transparent)
        qp = QtGui.QPainter(pm)
        if self._clipRadius > 1:
            path = QtGui.QPainterPath()
            path.addRect(rect)
            size = self._clipRadius * 2 - 1
            mask = QtCore.QRectF(0, 0, size, size)
            mask.moveCenter(rect.center())
            path.addEllipse(mask)
            qp.setClipPath(path)
        qp.fillRect(rect, grad1)
        if grad2:
            qp.setCompositionMode(qp.CompositionMode_SourceAtop)
            qp.fillRect(rect, grad2)
        qp.end()
        return pm

    def _setDistance(self, distance):
        distance = max(1, distance)
        self._distance = distance
        if self._clipRadius > distance:
            self._clipRadius = distance
        distance += self._clipRadius
        r = QtCore.QRectF(0, 0, distance * 2, distance * 2)

        lightSideStops = self.lightSideStops[:]
        shadowSideStops = self.shadowSideStops[:]
        if self._clipRadius:
            gradStart = self._clipRadius / (self._distance + self._clipRadius)
            lightSideStops[0] = (gradStart, lightSideStops[0][1])
            shadowSideStops[0] = (gradStart, shadowSideStops[0][1])

        # create the 4 corners as if the light source was top-left
        self._radial.setStops(lightSideStops)
        topLeft = self._getCornerPixmap(r, self._radial)

        self._conical.setAngle(359.9)
        self._conical.setStops(self.cornerStops)
        topRight = self._getCornerPixmap(r.translated(-distance, 0), self._radial, self._conical)

        self._conical.setAngle(270)
        self._conical.setStops(self.cornerStops)
        bottomLeft = self._getCornerPixmap(r.translated(0, -distance), self._radial, self._conical)

        self._radial.setStops(shadowSideStops)
        bottomRight = self._getCornerPixmap(r.translated(-distance, -distance), self._radial)

        # rotate the images according to the actual light source
        images = topLeft, topRight, bottomRight, bottomLeft
        shift = self._cornerShift.index(self._origin)
        if shift:
            transform = QtGui.QTransform().rotate(shift * 90)
            for img in images:
                img.swap(img.transformed(transform, QtCore.Qt.SmoothTransformation))

        # and reorder them if required
        self.topLeft, self.topRight, self.bottomRight, self.bottomLeft = images[-shift:] + images[:-shift]

    def origin(self):
        return self._origin

    @QtCore.pyqtSlot(QtCore.Qt.Corner)
    def setOrigin(self, origin):
        origin = QtCore.Qt.Corner(origin)
        if origin == self._origin:
            return
        self._setOrigin(origin)
        self._setDistance(self._distance)
        self.update()
        self.originChanged.emit(self._origin)

    def _setOrigin(self, origin):
        self._origin = origin

        gradients = self._leftGradient, self._topGradient, self._rightGradient, self._bottomGradient
        stops = self.lightSideStops, self.lightSideStops, self.shadowSideStops, self.shadowSideStops

        # assign color stops to gradients based on the light source position
        shift = self._cornerShift.index(self._origin)
        for grad, stops in zip(gradients, stops[-shift:] + stops[:-shift]):
            grad.setStops(stops)

    def clipRadius(self):
        return self._clipRadius

    @QtCore.pyqtSlot(int)
    @QtCore.pyqtSlot(float)
    def setClipRadius(self, radius):
        if radius == self._clipRadius:
            return
        oldRadius = self._clipRadius
        self._setClipRadius(radius)
        self.update()
        if oldRadius != self._clipRadius:
            self.clipRadiusChanged.emit(self._clipRadius)

    def _setClipRadius(self, radius):
        radius = min(self._distance, max(0, int(radius)))
        self._clipRadius = radius
        self._setDistance(self._distance)

    def boundingRectFor(self, rect):
        d = self._distance + 1
        return rect.adjusted(-d, -d, d, d)

    def draw(self, qp):
        restoreTransform = qp.worldTransform()

        qp.setPen(QtCore.Qt.NoPen)
        x, y, width, height = self.sourceBoundingRect(QtCore.Qt.DeviceCoordinates).getRect()
        right = x + width
        bottom = y + height
        clip = self._clipRadius
        doubleClip = clip * 2

        qp.setWorldTransform(QtGui.QTransform())
        leftRect = QtCore.QRectF(x - self._distance, y + clip, self._distance, height - doubleClip)
        qp.setBrush(self._leftGradient)
        qp.drawRect(leftRect)

        topRect = QtCore.QRectF(x + clip, y - self._distance, width - doubleClip, self._distance)
        qp.setBrush(self._topGradient)
        qp.drawRect(topRect)

        rightRect = QtCore.QRectF(right, y + clip, self._distance, height - doubleClip)
        qp.setBrush(self._rightGradient)
        qp.drawRect(rightRect)

        bottomRect = QtCore.QRectF(x + clip, bottom, width - doubleClip, self._distance)
        qp.setBrush(self._bottomGradient)
        qp.drawRect(bottomRect)

        qp.drawPixmap(x - self._distance, y - self._distance, self.topLeft)
        qp.drawPixmap(right - clip, y - self._distance, self.topRight)
        qp.drawPixmap(right - clip, bottom - clip, self.bottomRight)
        qp.drawPixmap(x - self._distance, bottom - clip, self.bottomLeft)

        qp.setWorldTransform(restoreTransform)
        if self._clipRadius:
            path = QtGui.QPainterPath()
            source, offset = self.sourcePixmap(QtCore.Qt.DeviceCoordinates)

            sourceBoundingRect = self.sourceBoundingRect(QtCore.Qt.DeviceCoordinates)
            qp.save()
            qp.setTransform(QtGui.QTransform())
            path.addRoundedRect(sourceBoundingRect, self._clipRadius, self._clipRadius)
            qp.setClipPath(path)
            qp.drawPixmap(source.rect().translated(offset), source)
            qp.restore()
        else:
            self.drawSource(qp)