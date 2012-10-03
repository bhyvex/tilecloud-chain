openlayers_html = """<!DOCTYPE html>
<html>
  <head>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=0">
    <meta name="apple-mobile-web-app-capable" content="yes">
    <title>OpenLayers test page</title>
    <link rel="stylesheet" href="http://openlayers.org/dev/theme/default/style.css" type="text/css">
    <style>
        html, body, #map {
            width: 100%;
            height: 100%;
            margin: 0;
        }
        #attrs {
            position: absolute;
            bottom: 1em;
            left: 1em;
        }
    </style>
</head>
<body>
    <div id="map">
        <div id="attrs">hi</div>
    </div>
    <script src="OpenLayers.js"></script>
    <script src="wmts.js"></script>
</body>
</html>"""
