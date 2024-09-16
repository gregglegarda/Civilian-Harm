import dash
import dash_html_components as html
external_css = ['https://cesium.com/downloads/cesiumjs/releases/1.76/Build/Cesium/Widgets/widgets.css']

app = dash.Dash(__name__,
                title='Cesium Test',
                external_stylesheets=external_css)

app.layout = html.Div(id='blah',
                      children=[
                          'Testing...',
                          html.Script(src='https://cesium.com/downloads/cesiumjs/releases/1.76/Build/Cesium/Cesium.js'),
                          html.Div(id='cesiumContainer'),
                          html.Script('''
          Cesium.Ion.defaultAccessToken = 'any_code_works';
          var viewer = new Cesium.Viewer('cesiumContainer');
                          ''')
                      ])

if __name__ == '__main__':
    app.run_server(debug=True, use_reloader=False)