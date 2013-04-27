$(document).ready(function() {

	/* Apply fancybox to multiple items */
	
	$('a.image-gallery:not(.link)').fancybox({
		'transitionIn'	:	'elastic',
		'transitionOut'	:	'elastic',
		'speedIn'		:	600, 
		'speedOut'		:	200, 
		'overlayShow'	:	false
	});
	
});
