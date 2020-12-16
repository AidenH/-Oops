$(document).ready(function() {

  //Add button
  $('#addbutton').on('mouseover', function() {
    $('#addbutton').addClass('hover');
  })

  $('#addbutton').on('mouseout', function() {
    $('#addbutton').removeClass('hover');
  })

  //Delete button
  $('.delete').on('mouseover', function() {
    $('.delete').addClass('hover');
  })

  $('.delete').on('mouseout', function() {
    $('.delete').removeClass('hover');
  })

});
