'''pyQt 6 App with shadertoy

'''
import sys
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtOpenGLWidgets import QOpenGLWidget
from PyQt6.QtCore import QElapsedTimer
from OpenGL import GL
from PyQt6.QtOpenGL import QOpenGLShaderProgram, QOpenGLShader  # Ensure correct import

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
        self.elapsed_timer = QElapsedTimer()

    def initializeGL(self):
        self.program = QOpenGLShaderProgram(self.context())
        self.program.addShaderFromSourceCode(QOpenGLShader.ShaderTypeBit.Vertex, vertex_shader_source)  # Correct shader type
        self.program.addShaderFromSourceCode(QOpenGLShader.ShaderTypeBit.Fragment, fragment_shader_source)  # Correct shader type
        self.program.link()
        self.program.bind()
        vertices = [-1.0, -1.0, 1.0, -1.0, -1.0, 1.0, 1.0, 1.0]
        vertices = (GL.GLfloat * len(vertices))(*vertices)
        self.vbo = GL.glGenBuffers(1)
        GL.glBindBuffer(GL.GL_ARRAY_BUFFER, self.vbo)
        GL.glBufferData(GL.GL_ARRAY_BUFFER, len(vertices) * 4, vertices, GL.GL_STATIC_DRAW)
        position_location = self.program.attributeLocation("position")
        self.program.enableAttributeArray(position_location)
        GL.glVertexAttribPointer(position_location, 2, GL.GL_FLOAT, GL.GL_FALSE, 0, None)
        self.program.release()
        self.elapsed_timer.start()

    def paintGL(self):
        GL.glClear(GL.GL_COLOR_BUFFER_BIT | GL.GL_DEPTH_BUFFER_BIT)
        current_time = self.elapsed_timer.elapsed() / 1000.0
        self.program.bind()
        self.program.setUniformValue(self.program.uniformLocation("iTime"), current_time)
        GL.glBindBuffer(GL.GL_ARRAY_BUFFER, self.vbo)
        position_location = self.program.attributeLocation("position")
        GL.glEnableVertexAttribArray(position_location)
        GL.glDrawArrays(GL.GL_TRIANGLE_STRIP, 0, 4)
        GL.glDisableVertexAttribArray(position_location)
        self.program.release()

    def resizeGL(self, w, h):
        GL.glViewport(0, 0, w, h)

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





