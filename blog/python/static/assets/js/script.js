( function( $ ) {
$( document ).ready(function() {
$('#cssmenu').prepend('<div id="menu-button">Menu</div>');
	$('#cssmenu #menu-button').on('click', function(){
		var menu = $(this).next('ul');
		if (menu.hasClass('open')) {
			menu.removeClass('open');
		}
		else {
			menu.addClass('open');
		}
	});
});
} )( jQuery );

function initPageSelector(){  
	activePageButton();  
	initSelectPage();  
}  
function activePageButton(){  
	$(".li_btn").click(function(){  
		$(".li_btn").css("background-color","#fff");  
		$(".li_btn").css("color","#858585");  
		$(this).css("background-color","#00bcd4");  
		$(this).css("color","#fff");  
	});  
}  
function initSelectPage(){  
	$(".li_next").click(function(){  
		document.getElementById("div_li_btn_mid").scrollLeft+=40;  
	});  
	$(".li_prew").click(function(){  
		document.getElementById("div_li_btn_mid").scrollLeft-=40;  
	});  
}  
