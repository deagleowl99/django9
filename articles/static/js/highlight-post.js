$(document).ready(function(){
	$('.one-post').hover(function(event){
		console.log("Навели");
	},
	function(event){
		console.log("Вывели");
	});
});

$(document).ready(function(){
	$('.one-post').hover(function(event){
		$(event.currentTarget).find('.one-post-shadow').animate({opacity: '0.1'}, 100);
	},
	function(event){
		$(event.currentTarget).find('.one-post-shadow').animate({opacity: '0'}, 100);
	})
});

$(document).ready(function(){    
   $('.image').hover(function(event){        
      $(event.currentTarget).animate({width:'520'},300);    
      $(this).attr('src','static/img/dpb-logo.png'); 
   }, function(event){
    $(event.currentTarget).animate({width:'179'},300);
    $(this).attr('src','static/img/dpb-logo.png');
   })
});

$(document).ready(function(){
    var yPosition;
    var scrolled = 0;
    var $parallaxElements = $('.icons-for-parallax img');
    var $parallaxElement = $('.image');
    $(window).scroll(function() { 
       scrolled = $(window).scrollTop(); 
       for (var i = 0; i < $parallaxElements.length; i++){ 
	   yPosition = (scrolled * 0.15*i); 
          $parallaxElements.eq(i).css({ top: yPosition }); 
       }
       yPosition = (scrolled * 0.95);
       $parallaxElement.eq(0).css({ top: yPosition });
    }); 
}); 
