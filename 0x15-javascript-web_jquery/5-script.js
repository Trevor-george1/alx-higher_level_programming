// adds a list element whrn user clicks on tag DIV#add_item

const listitem = $('<li>').text('Item');
$('DIV#add_item').on('click', function () {
  $('.my_list').append(listitem);
});
