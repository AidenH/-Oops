
// TILE CONTROLS

function tileEditable(id) {
  document.getElementById(id).contentEditable = true;
}

function tileUpdate(tile_id = 0) {
  var content_updated = document.getElementById(tile_id).innerHTML;
  $.ajax({
    url: "tile-update/",
    data: {
      'id': tile_id,
      'content': content_updated
    },
    success: function() {
      console.log("Update success.");
    }
    });
}

function addTile() {
  console.log("add tile");
  $.ajax({
    url: "tile-add/",
    success: function() {
      console.log("Add tile success.");
      location.reload();
    }
  })
}

function deleteTile(tile_id) {
  console.log("delete tile #" + tile_id)
  $.ajax({
    url: "tile-delete/",
    data: {
      'id': tile_id
    },
    success: function() {
      console.log("deleteTile success.");
      location.reload();
    }
  })
}
