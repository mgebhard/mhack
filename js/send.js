
var prev_img;
var final_src;

var GetFlickrUrl = function(photo) {
  return 'http://farm' + photo.farm +
         '.staticflickr.com/' + photo.server +
         '/' + photo.id + '_' + photo.secret + '.jpg';
}

var AddPhoto = function(photo) {
  $("#photos").append("<img class='pic' onclick='HighlightImg(this)' src=\"" + GetFlickrUrl(photo) + "\">");
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
	final_src = null;
    var term = $("#searchbox").val();
	var flickr = "http://api.flickr.com/services/rest/?method=flickr.photos.search&api_key=d35f6537258f506e4f84c84a16bb13e8&format=json&jsoncallback=?";
	var params = { "tags": term };
	$.getJSON(flickr, params, DisplayPhotos);
	
	// Update the search term in HTML
	$('#searchterm').text(term);
	$('#intro').show();
};

var validateForm = function(form){
	//Add img src to form before submit
	if (final_src != null){
	var input = document.createElement("input");
	input.setAttribute("type", "hidden");
	input.setAttribute("name", "pic_src");
	input.setAttribute("value", final_src);
	form.appendChild(input);
	}	
	else{
		alert("Make sure you have a picture selected.");
		return false;
	}

	var friend = document.getElementById('send')
	var answer = document.getElementById('ans')
	if (friend.value != "" && answer.value != ""){
		form.submit();
	}
	else{
		alert("Make sure you have the To and answer filled out.");
		return false;
	}

	};

var HighlightImg = function(img){
	if (prev_img != null){
	prev_img.style.border = '0';
	}
	img.style.border = "2px outset #3399FF";

	final_src = img.src;
	prev_img = img;
};

var Main = function() {
	$('#load').click(FetchAndDisplayPhotos);
	$('#intro').hide();
};

$(document).ready(Main);
