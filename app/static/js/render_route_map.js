function renderRouteMap(containerId, encodedPolyline, options = {}) {
  const {
    precision = 5,
    color = "#FC5201",
    weight = 5,
    weight_border = 8
  } = options;

  if (!encodedPolyline) return;

  const el = document.getElementById(containerId);
  if (!el) return;

  let latlngs;
  try {
    latlngs = polyline.decode(encodedPolyline, precision);
  } catch (e) {
    console.error("Polyline decode error:", containerId, e);
    return;
  }

  const map = L.map(containerId, {
    zoomControl: true,
    attributionControl: true
  });

  L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 19
  }).addTo(map);

  const routeOutline = L.polyline(latlngs, {
    color: "#fff",
    weight: weight_border,
    opacity: 1
  }).addTo(map);

  const route = L.polyline(latlngs, {
    color: color,
    weight: weight,
    opacity: 1
  }).addTo(map);

  map.fitBounds(route.getBounds(), { padding: [20, 20] });

  L.marker(latlngs[0], { icon: dotIcon(color) }).addTo(map).bindPopup("Старт");
  L.marker(latlngs[latlngs.length - 1], { icon: dotIcon(color) }).addTo(map).bindPopup("Финиш");

  return { map, route };
}

function dotIcon(color) {
  return L.divIcon({
    className: "",
    iconSize: [16, 16],
    iconAnchor: [8, 8],
    html: `<div style="
      width:16px;
      height:16px;
      border-radius:50%;
      background:${color};
      border:2px solid #fff;
      box-shadow:0 1px 4px rgba(0,0,0,.45);
    "></div>`
  });
}