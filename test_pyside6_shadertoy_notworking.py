'''pyQt 6 App with shadertoy

'''
import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtOpenGLWidgets import QOpenGLWidget
from PySide6.QtCore import QElapsedTimer
from OpenGL import GL
from PySide6.QtGui import QSurfaceFormat
from PySide6.QtOpenGLWidgets import QOpenGLWidget
from PySide6.QtOpenGL import QOpenGLShaderProgram, QOpenGLShader
from PySide6.QtOpenGL import QOpenGLVertexArrayObject, QOpenGLBuffer
import numpy as np

vertex_shader_source = """
#version 330
in vec2 position;
void main() {
    gl_Position = vec4(position, 0.0, 1.0);
}
"""

fragment_shader_source = """
#version 330
uniform float iTime;
out vec4 fragColor;
void main() {
    vec2 uv = gl_FragCoord.xy / vec2(1920, 1080);
    vec3 col = 0.5 + 0.5 * cos(iTime + uv.xyx + vec3(0, 2, 4));
    fragColor = vec4(col, 1.0);
}
"""


class ShaderToyWidget(QOpenGLWidget):
    def __init__(self):
        super().__init__()
        format = QSurfaceFormat()
        format.setVersion(3, 3)
        format.setProfile(QSurfaceFormat.CoreProfile)
        self.setFormat(format)
        self.program = None
        self.vao = None
        self.vbo = None
        self.gl = self.context().versionFunctions()


        self.elapsed_timer = QElapsedTimer()

    def initializeGL(self):
        if not self.context().isValid():
            print("OpenGL context is not valid")
            return
        self.gl = self.context().functions()
        
        self.program = QOpenGLShaderProgram(self)
        self.program.addShaderFromSourceCode(QOpenGLShader.Vertex, vertex_shader_source)
        self.program.addShaderFromSourceCode(QOpenGLShader.Fragment, fragment_shader_source)
        if not self.program.link():
            print("Shader program linking failed:", self.program.log())
        
        self.vao = QOpenGLVertexArrayObject(self)
        self.vao.create()
        self.vao.bind()
        
        vertices = [-1.0, -1.0, 1.0, -1.0, -1.0, 1.0, 1.0, 1.0]
        self.vbo = QOpenGLBuffer()
        self.vbo.create()
        self.vbo.bind()
        self.vbo.allocate(np.array(vertices, dtype=np.float32).tobytes(), len(vertices) * 4)
        
        self.program.bind()
        position_location = self.program.attributeLocation("position")
        self.gl.glEnableVertexAttribArray(position_location)
        self.gl.glVertexAttribPointer(position_location, 2, self.gl.GL_FLOAT, self.gl.GL_FALSE, 0, None)
        
        self.vao.release()
        self.program.release()
        self.vbo.release()
        
        self.elapsed_timer.start()

    def paintGL(self):
        self.gl.glClear(self.gl.GL_COLOR_BUFFER_BIT | self.gl.GL_DEPTH_BUFFER_BIT)
        current_time = self.elapsed_timer.elapsed() / 1000.0
        
        self.program.bind()
        self.vao.bind()
        
        self.program.setUniformValue(self.program.uniformLocation("iTime"), current_time)
        self.gl.glDrawArrays(self.gl.GL_TRIANGLE_STRIP, 0, 4)
        
        self.vao.release()
        self.program.release()
        
        self.update()

    def resizeGL(self, w, h):
        self.gl.glViewport(0, 0, w, h)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setCentralWidget(ShaderToyWidget())
        self.resize(1920, 1080)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())


'''
        self.program.addShaderFromSourceCode(QOpenGLShader.ShaderTypeBit.Vertex, vertex_shader_source)
        self.program.addShaderFromSourceCode(QOpenGLShader.ShaderTypeBit.Fragment, fragment_shader_source)
        
        '''
