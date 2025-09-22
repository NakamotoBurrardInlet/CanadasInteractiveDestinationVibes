document.addEventListener('DOMContentLoaded', function () {
    // 1. Initialize the map
    // Centered on Canada [lat, long], zoom level
    const map = L.map('map').setView([56.1304, -106.3468], 4);

    // 2. Add a tile layer (the map background)
    L.tileLayer('https://{s}.basemaps.cartocdn.com/dark_all/{z}/{x}/{y}{r}.png', {
        attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors &copy; <a href="https://carto.com/attributions">CARTO</a>',
        subdomains: 'abcd',
        maxZoom: 19
    }).addTo(map);

    // 3. Fetch destination data from our Flask API
    fetch('/api/destinations')
        .then(response => response.json())
        .then(data => {
            // 4. Loop through the data and add markers
            data.forEach(destination => {
                const marker = L.marker(destination.coords).addTo(map);
                
                // 5. Create a popup for each marker
                marker.bindPopup(`
                    <b>${destination.name}</b><br>
                    Avg. Hotel: $${destination.avg_hotel_price}/night
                `);
            });
        })
        .catch(error => console.error('Error fetching destination data:', error));
});
