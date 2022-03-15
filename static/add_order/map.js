let map;
let input;
let place;
function initMap() {
    map = new google.maps.Map(document.getElementById("map"), {
        center: { lat: 6.247, lng:  -75.565 },
        zoom: 10,
    });
    input = document.getElementById('id_place_name');
    const options = {
        fields: ["place_id", "formatted_address", "geometry", "name"],
        strictBounds: false,
        //componentRestrictions: { country: ["co"] },
        types: ["establishment"],
      };
      
    autocomplete = new google.maps.places.Autocomplete(input,options);
    autocomplete.bindTo("bounds",map);


    // Defining Marker
    const marker = new google.maps.Marker({ map: map });
    
    
    
    autocomplete.addListener("place_changed", () => {
        marker.setVisible(false);
        place = autocomplete.getPlace();
        
        if (!place.geometry || !place.geometry.location) {
            // User entered the name of a Place that was not suggested and
            // pressed the Enter key, or the Place Details request failed.
            window.alert("No details available for input: '" + place.name + "'");
            document.getElementById('id_place_name').value = ""
            return;
        }

        if (place.geometry.viewport) {
            map.fitBounds(place.geometry.viewport);
        } else {
            map.setCenter(place.geometry.location);
            map.setZoom(17);
        }

        marker.setPosition(place.geometry.location);
        marker.setVisible(true);
    });
    document.getElementById('id_place_name').addEventListener('change', (e) => {
        place = e.target.value
    })
}
function submitForm(event){
    //event.preventDefault();
    if (!place.hasOwnProperty('place_id')){
        // User entered the name of a Place that was not suggested and
        // pressed the Enter key, or the Place Details request failed.
        window.alert("Select an address from the dropdown");
        document.getElementById('id_place_id').value = ""
        return False;
    } else {
        document.getElementById('id_place_name').value = place['name'];
        document.getElementById('id_place_address').value = place['formatted_address'];
        document.getElementById('id_place_id').value = place['place_id'];
        return True;
    }
}