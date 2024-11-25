const tracksElement = document.getElementById('tracks');




const tracksData = {
  // Replace this with your actual JSON data
  "tracks": [
    {
      "album": {
        "name": "In The Lonely Hour (Deluxe)"
      },
      "artists": [
        {
          "name": 'Sam smith'
        }
      ],
      "track_name": "Money On My Mind",
      "external_urls": {
        "spotify": "https://open.spotify.com/track/15HsdLcI9txtlLpsHBbEjn"
      },
        "spotify_song_id": "0rzNMzZsubFcXSEh7dnem7",
        "time_signature": 4,
        "key": 0,
        "mode": 1,
        "tempo": 80.744,
        "artist": "beyonce",
        "song": "holdup",

    },
    // ... other track objects
  ]
};





function displayTracks(tracks) {
  tracks.forEach(track => {
    const trackElement = document.createElement('div');
    trackElement.classList.add('track');

    let html = `<h4>${track.name}</h4>`;
    html += `<a href="${track.external_urls.spotify}" target="_blank">`;
    if (track.album && track.album.images) {
      html += `<img src="${track.album.images[0].url}" alt="${track.album.name} cover">`;
    } else {
      html += `<p>No album image available</p>`;
    }
    html += `</a>`;
    html += `<p>By ${track.artists[0].name}</p>`;

    trackElement.innerHTML = html;
    tracksElement.appendChild(trackElement);
  });
}

displayTracks(tracksData.tracks);


fetch('output.json')
  .then(response => response.json())
  .then(track => {
    // Access your JSON data here



//    console.log(track.spotify_song_id);


    //format html

    //image and album
    let html = `<h4>${track.title}</h4>`;
    if (track.album && track.album.images) {
        html += `<img src="${track.album.images[0].url}" alt="${track.album.name} cover">`;
      } else {
        html += `<p>No album image available</p>`;
      }
      html += `</a>`;
        html += `<p>By ${track.artist}</p>`;
        html += `<p>By ${track.song}</p>`;
        // html += `<a href="${track.external_urls.spotify}" target="_blank">`;
        html += `<p>Tempo is: ${track.tempo}</p>`;
        html += `<p>Time signature is: ${track.time_signature}</p>`;
        html += `<p>Mode is: ${track.mode}</p>`;
        html += `<p>Key is: ${track.key}</p>`;


    document.write(html)
    
    
  })
  .catch(error => {
    // Handle errors here
    console.error('Error fetching JSON:', error);
  });
