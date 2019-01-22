// jQuery v3.3.1 is supported
$('.pic').click(function() {
	$(this).toggleClass('active');
	$('.backdrop').toggleClass('underlay');
});