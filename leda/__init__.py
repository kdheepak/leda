from IPython.core.display import display, HTML, Javascript
from jinja2 import Template

_loaded = {'d3': False, 'gmaps': False}

def enable(d3=True, gmaps=False):

    if d3 and not _loaded['d3']:
        enable_d3()
        _loaded['d3'] = True
    if gmaps and not _loaded['gmaps']:
        enable_gmaps()
        _loaded['gmaps'] = True


def enable_d3(version=3):

    string= Template("""
    require.config({
    paths: {
        d3: "https://d3js.org/d3.v{{version}}.min"
     }
    });

    require(["d3"], function(d3) {

    window.d3 = d3

    console.log('Loaded d3 version ' + d3.version);

    });
    """).render(version=version)
    display(Javascript(string))


def enable_gmaps():

    string = Template("""
    <script src="https://maps.google.com/maps/api/js?sensor=true"></script>
    """).render()
    display(HTML(string))


def render_html(string, **kwargs):
    '''
    html_string = """
    <svg width="400" height="200"></svg>
    """
    '''
    string = Template(string).render(**kwargs)
    display(HTML(string))

def render_js(string, **kwargs):

    string = Template(string).render(**kwargs)

    display(Javascript(string))
