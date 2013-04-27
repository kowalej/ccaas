$(document).ready(function () {
	
	//Top nav menu setup
	$('ul#menu li a#current').parent().children('ul').css('visibility', 'visible');
	var current_sub_menu = $('ul#menu li a.current').parent();
	var primary_content_width = $('.primary-content').width();
	var secondary_content_width = $('.secondary-content').width();
	var tertiary_content_width = $('.tertiary-content').width();
	var main_width = $('#main').width();

	setup();

	function setup() {
		if(getCookie("cc-side-content") == 0){
			closeSideContent();
		}
	}

	function setCookie(name,value,days) {
		if (days) {
		    var date = new Date();
		    date.setTime(date.getTime()+(days*24*60*60*1000));
		    var expires = "; expires="+date.toGMTString();
		} else var expires = "";
		
		document.cookie = name+"="+value+expires+"; path=/";
	}

	function getCookie(name) {
		var nameEQ = name + "=";
		var ca = document.cookie.split(';');
		for(var i=0;i < ca.length;i++) {
			var c = ca[i];
			while (c.charAt(0)==' ') c = c.substring(1,c.length);
			if (c.indexOf(nameEQ) == 0) return c.substring(nameEQ.length,c.length);
		}
		return null;
	}

	function deleteCookie(name) {
		setCookie(name,"",-1);
	}

	function openSideContent() {
		$('div.primary-content').width(primary_content_width);
        $('div.primary-content').css({'margin-left': '20px', 'float': 'left'});
		$('div.secondary-content').width(secondary_content_width);
		$('div#secondary-content-show').toggle();
		$('div#secondary-content-hide').toggle();
		$('div.secondary-content').toggle(); 
		setCookie("cc-side-content", 1);
	}

	function closeSideContent() {
		$('div.secondary-content').toggle();
		$('div.primary-content').width(main_width - $('div.tertiary-content').width() - 24);
        $('div.primary-content').css({'margin-left': '0px', 'float': 'right'});
        $('div.primary-content').width
		$('div#secondary-content-show').toggle();
		$('div#secondary-content-hide').toggle();
		setCookie("cc-side-content", 0);
	}
	
	$('ul#menu ul').slice(1).each(function () {
		var parent_mid_x = $(this).parent().width()/2;
	 	var child_mid_x = $(this).width()/2; 

		var center_offset = parent_mid_x - child_mid_x;
        $(this).css('margin-left' , center_offset);

        var overhang_right = ($('ul#menu').offset().left + $('ul#menu').width()) - ($(this).offset().left + $(this).width()); 

		if(overhang_right < 0) {
			var new_center_offset = center_offset + overhang_right;
			$(this).css('margin-left' , new_center_offset - 2);
		}
	});

	$('ul#menu > li').not(current_sub_menu).has('ul li').hover(
		function () {
			$('ul#menu li a.current').parent().children('ul').css('visibility', 'hidden');
		},

		function () {
			$('ul#menu li a.current').parent().children('ul').css('visibility', 'visible');
		}
	);	

	//Actions
	$('div#secondary-content-hide').click(function() {
		closeSideContent();	
	});

	$('div#secondary-content-show').click(function() {
		openSideContent();
	});

	$('#messages a').click(function() {
		$(this).parent().hide();
		return false;
	});

}); 
