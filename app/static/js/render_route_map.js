function renderRouteMap(containerId, encodedPolyline, options = {}) {
  const {
    precision = 5,
    color = '#1a73e8',
    weight = 5
  } = options;

  if (!encodedPolyline) return;

  const el = document.getElementById(containerId);
  if (!el) return;

  // Декодируем polyline -> [[lat,lng], ...]
  let latlngs;
  try {
    latlngs = polyline.decode(encodedPolyline, precision);
  } catch (e) {
    console.error("Polyline decode error:", containerId, e);
    return;
  }

  // Создаём карту
  const map = L.map(containerId, {
    // zoomControl: true,
    // attributionControl: true
  });

  L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 19
  }).addTo(map);

  const route = L.polyline(latlngs, { color, weight }).addTo(map);
  map.fitBounds(route.getBounds(), { padding: [20, 20] });

  L.marker(latlngs[0]).addTo(map).bindPopup("Старт");
  L.marker(latlngs[latlngs.length - 1]).addTo(map).bindPopup("Финиш");

  return { map, route };
}