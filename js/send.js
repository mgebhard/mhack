var GetFlickrUrl = function(photo) {
  return 'http://farm' + photo.farm +
         '.staticflickr.com/' + photo.server +
         '/' + photo.id + '_' + photo.secret + '.jpg';
}

var AddPhoto = function(photo) {
  $("#photos").append("<img class='pic' onclick='SendImg(this.src)' src=\"" + GetFlickrUrl(photo) + "\">");
};

var AddAllPhotos = function(photos) {
  for (i in photos) {
    AddPhoto(photos[i]);
  }
};

var DisplayPhotos = function(flickrPhotos) {
   $("#photos").empty();
   AddAllPhotos(flickrPhotos.photos.photo);
};

var FetchAndDisplayPhotos = function() {
    var term = $("#searchbox").val();
	var flickr = "http://api.flickr.com/services/rest/?method=flickr.photos.search&api_key=d35f6537258f506e4f84c84a16bb13e8&format=json&jsoncallback=?";
	var params = { "tags": term };
	$.getJSON(flickr, params, DisplayPhotos);
	
	// Update the search term in HTML
	$('#searchterm').text(term);
	$('#intro').show();
};

var SendImg = function(pic_src){
	var input = document.createElement("input");
	input.setAttribute("type", "hidden");
	input.setAttribute("name", "pic_src");
	input.setAttribute("value", pic_src);
	var form = document.getElementById("picsend")
	
	form.appendChild(input);

	var friend = document.getElementById('send')
	var answer = document.getElementById('ans')
	if (friend.value != "" && answer.value != ""){
		form.submit();
	}
	else{
		alert("Make sure you have the To and answer filled out!");
	}

	};

var Main = function() {
	$('#load').click(FetchAndDisplayPhotos);
	$('#intro').hide();
};

	$(document).ready(Main);
</script>