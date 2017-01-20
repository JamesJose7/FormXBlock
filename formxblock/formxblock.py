"""TO-DO: Write a description of what this XBlock is."""

import pkg_resources

from xblock.core import XBlock
from xblock.fields import Scope, Integer, String, Boolean
from xblock.fragment import Fragment


class FormXBlock(XBlock):
    
    count = Integer(default=0, help="contador encuestas", scope=Scope.user_state_summary)
    usuario = String(help="Usuario open Campus", default=None, scope=Scope.user_state)
    pais = String(help="Pais usuario", default=None, scope=Scope.user_state)
    ciudad = String(help="ciudad usuario", default=None, scope=Scope.user_state)
    lugarInv = String(help="Lugar investigacion", default=None, scope=Scope.user_state)
    descripcionLugar = String(help="Descripcion del lugar", default=None, scope=Scope.user_state)
    textura = String(help="Textura", default=None, scope=Scope.user_state)
    ph = String(help="ph investigacion", default=None, scope=Scope.user_state)
    materiaOrg = String(help="Materia organica", default=None, scope=Scope.user_state)
    nitrogeno = String(help="Nitrogeno", default=None, scope=Scope.user_state)
    reflexion = String(help="Breve reflexion de los parametros consultas", default=None, scope=Scope.user_state)
    bibliografia = String(help="Bibliografia", default=None, scope=Scope.user_state)
    observaciones = String(help="Observaciones", default=None, scope=Scope.user_state)

    tookSurvey = Boolean(help="Has this student taken the survey?", default=False, scope=Scope.user_state)
    
    def resource_string(self, path):
        """Handy helper for getting resources from our kit."""
        data = pkg_resources.resource_string(__name__, path)
        return data.decode("utf8")

    def student_view(self, context=None):
        """
        The primary view of the FormXBlock, shown to students
        when viewing courses.
        """
        html = self.resource_string("static/html/formxblock.html")
        frag = Fragment(html.format(self=self))
        frag.add_css(self.resource_string("static/css/formxblock.css"))
        frag.add_javascript(self.resource_string("static/js/src/formxblock.js"))
        frag.initialize_js('FormXBlock')
        return frag

    @XBlock.json_handler
    def test_func(self, data, suffix=''):

        #Asignacion de campos a datos
        self.usuario = data['datos'][0]
        self.pais = data['datos'][1]
        self.ciudad = data['datos'][2]
        self.lugarInv = data['datos'][3]
        self.descripcionLugar = data['datos'][4]
        self.textura = data['datos'][5]
        self.ph = data['datos'][6]
        self.materiaOrg = data['datos'][7]
        self.nitrogeno = data['datos'][8]
        self.reflexion = data['datos'][9]
        self.bibliografia = data['datos'][10]
        self.observaciones = data['datos'][11]

        self.tookSurvey = True
        self.count += 1

        return {"count": self.count}

    @XBlock.json_handler
    def get_count(self, data, suffix=''):

        return {"count": self.count}

    @staticmethod
    def workbench_scenarios():
        """A canned scenario for display in the workbench."""
        return [
            ("FormXBlock",
             """<formxblock/>
             """),
            ("Multiple FormXBlock",
             """<vertical_demo>
                <formxblock/>
                <formxblock/>
                <formxblock/>
                </vertical_demo>
             """),
        ]
