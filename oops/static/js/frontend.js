//Separate function for enlarging delete buttons. Had to add here in order
//to pass unique tile id to function for a particular delete button.
function deleteHover(tile_id) {
  console.log(tile_id);
  $('#delete'+tile_id).addClass('hover');
}

$(document).ready(function() {

  //Add button
  $('#addbutton').on('mouseover', function() {
    $('#addbutton').addClass('hover');
  })

  $('#addbutton').on('mouseout', function() {
    $('#addbutton').removeClass('hover');
  })

  //Old delete button mouseover function.
  /*$('.delete').on('mouseover', function(tile_id) {
    console.log(tile_id);
    $('.delete').addClass('hover');
  })*/

  //Delete mouseout left the same because we don't need to use a specific
  //delete button.
  $('.delete').on('mouseout', function() {
    $('.delete').removeClass('hover');
  })

});
