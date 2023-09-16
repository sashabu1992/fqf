/**
 * @package Helix3 Framework
 * @template Shaper Empire
 * @author JoomShaper http://www.joomshaper.com
 * @copyright Copyright (c) 2010 - 2016 JoomShaper
 * @license http://www.gnu.org/licenses/gpl-2.0.html GNU/GPLv2 or later
 */
jQuery(function ($) {

    $('#offcanvas-toggler').on('click', function (event) {
        event.preventDefault();
        $('body').addClass('offcanvas');
    });

    $('<div class="offcanvas-overlay"></div>').insertBefore('.body-innerwrapper > .offcanvas-menu');

    $('.close-offcanvas, .offcanvas-overlay').on('click', function (event) {
        event.preventDefault();
        $('body').removeClass('offcanvas');
    });

    var stopBubble = function (e) {
        e.stopPropagation();
        return true;
    };

    //Mega Menu
    $('.sp-megamenu-wrapper').parent().parent().css('position', 'static').parent().css('position', 'relative');
    $('.sp-menu-full').each(function () {
        $(this).parent().addClass('menu-justify');
    });

    //Sticky Menu
    $(document).ready(function () {
        $("body.sticky-header").find('#sp-header').sticky({topSpacing: 0})
    });

    //Tooltip
    $('[data-toggle="tooltip"]').tooltip();

    $(document).on('click', '.sp-rating .star', function (event) {
        event.preventDefault();

        var data = {
            'action': 'voting',
            'user_rating': $(this).data('number'),
            'id': $(this).closest('.post_rating').attr('id')
        };

        var request = {
            'option': 'com_ajax',
            'plugin': 'helix3',
            'data': data,
            'format': 'json'
        };

        $.ajax({
            type: 'POST',
            data: request,
            beforeSend: function () {
                $('.post_rating .ajax-loader').show();
            },
            success: function (response) {
                var data = $.parseJSON(response.data);

                $('.post_rating .ajax-loader').hide();

                if (data.status == 'invalid') {
                    $('.post_rating .voting-result').text('You have already rated this entry!').fadeIn('fast');
                } else if (data.status == 'false') {
                    $('.post_rating .voting-result').text('Somethings wrong here, try again!').fadeIn('fast');
                } else if (data.status == 'true') {
                    var rate = data.action;
                    $('.voting-symbol').find('.star').each(function (i) {
                        if (i < rate) {
                            $(".star").eq(-(i + 1)).addClass('active');
                        }
                    });

                    $('.post_rating .voting-result').text('Thank You!').fadeIn('fast');
                }

            },
            error: function () {
                $('.post_rating .ajax-loader').hide();
                $('.post_rating .voting-result').text('Failed to rate, try again!').fadeIn('fast');
            }
        });
    });

    // testimonial pro
    $('.sppb-testimonial-pro .sppb-item').each(function () {
        var next = $(this).next();
        if (!next.length) {
            next = $(this).siblings(':first');
        }
        //next.children(':first-child').clone().appendTo($(this));

        if (next.next().length > 0) {
            next.next().children(':first-child').clone().appendTo($(this));
        } else {
            $(this).siblings(':first').children(':first-child').clone().appendTo($(this));
        }
    });

});

//For react template
jQuery(function ($) {
    var observer = new MutationObserver(function (mutations) {
        mutations.forEach(function (mutation) {
            var newNodes = mutation.addedNodes;
            if (newNodes !== null) {
                var $nodes = $(newNodes);

                $nodes.each(function () {
                    var $node = $(this);
                    $node.find('#slider').each(function () {
                        //Thumb Slider
                        if ($('#carousel').is('.flexslider')) {

                            // Thumb Gallery
                            var $sppbTgOptions = $('.sppb-tg-slider');

                            // Autoplay
                            var $autoplay = $sppbTgOptions.data('sppb-tg-autoplay');

                            // arrows
                            var $arrows = $sppbTgOptions.data('sppb-tg-arrows');

                            $('#carousel').flexslider({
                                animation: 'slide',
                                controlNav: true,
                                directionNav: $arrows,
                                animationLoop: false,
                                slideshow: $autoplay,
                                itemWidth: 320,
                                itemMargin: 0,
                                asNavFor: '#slider'
                            });

                            $('#slider').flexslider({
                                animation: "fade",
                                controlNav: false,
                                directionNav: $arrows,
                                animationLoop: false,
                                slideshow: $autoplay,
                                sync: "#carousel"
                            });

                        }
                        // END:: Thumb Slider

                    });
                });
            }
        });
    });

    var config = {
        childList: true,
        subtree: true
    };
    // Pass in the target node, as well as the observer options
    observer.observe(document.body, config);
});


// Слайдер

(function($) {
	$.fn.ancapitalPropertySlider = function(options) {
		options	= $.extend(true, {
			startElementSelector		: ':first',							// Селектор фильрации для набора элементов
		}, options)
		
		
		
		var
			self				= this,
			slider 			= $(this),
			elements		= undefined,
			active			= undefined,
			next				= undefined,
			prev				= undefined,
			popup			= undefined,
			buttons			= undefined,
			nextButton		= undefined,
			prevButton		= undefined;
		
		
		var	
			getNextElement		= function() {
				var
					next = active.next();
					
				if(next.length)	return next;
				else				return elements.first();
			},
			
			getPrevElement		= function() {
				var
					prev = active.prev();
					
				if(prev.length)	return prev;
				else				return elements.last();
			},
			
			addButtons				= function() {
				buttons		= $(document.createElement('div'));
				nextButton	= $(document.createElement('a'));
				prevButton	= $(document.createElement('a'));
				
				buttons.addClass('ancapitalPropertySliderButtons').append(nextButton, prevButton);
				nextButton.addClass('next').attr('href', 'javascript: void(0)');
				prevButton.addClass('prev').attr('href', 'javascript: void(0)');
				slider.append(buttons);
			},
			
			onEvents				= function() {
				if(elements)
					elements.on('click', elementsClickEvent);
				if(prevButton)
					$(prevButton).on('click', buttonsClickEvent);
				if(nextButton)
					$(nextButton).on('click', buttonsClickEvent);
			},
			
			offEvents				= function() {
				if(elements)
					elements.off('click', elementsClickEvent);
				if(prevButton)
					$(prevButton).off('click', buttonsClickEvent);
				if(nextButton)
					$(nextButton).off('click', buttonsClickEvent);
			};
		
		
		
		var	
			elementsClickEvent			= function(e) {
				var
					target	= $(this);
			
				if(target.is(active))			self.popupOpen();
				else if(target.is(next))		self.next();
				else if(target.is(prev))		self.prev();
				
				e.preventDefault();
				return false;
			},
			
			buttonsClickEvent			= function(e) {
				var
					target	= $(this);
				
				if(target.is(nextButton))			self.next();
				else if(target.is(prevButton))		self.prev();
				
				e.preventDefault();
				return false;
			};
			
			
			
		this.refresh		= function() {
			if(popup && popup.length) {
				self.popupClose();
				popup.remove();
				popup 		= undefined;
			}
			
			if(buttons) {
				buttons.remove();
				buttons 		= undefined;
			}
			
			offEvents();
			
			elements	= slider.children().not('.ancapitalPropertySliderButtons');
			if(elements.filter(active).length === 0)
				active			= elements.filter(options.startElementSelector)
		
			elements.removeClass('active next prev');
			next = getNextElement();
			prev = getPrevElement();
			
			active.addClass('active');
			next.addClass('next');
			prev.addClass('prev');
			
			addButtons();
			
			popup		= $(document.createElement('div'));
			popup.addClass('ancapitalPropertySliderPopup');
			$(document.body).append(popup);
			onEvents();
		}
		
		this.next		= function() {
			active	= next;
			self.refresh();
		}
		
		this.prev		= function() {
			active	= prev;
			self.refresh();
		}
		
		this.popupOpen		= function() {
			self.popupClose();

			popup.empty();
			popup.append(active.children('img').clone());
			$(document.body).addClass('ancapitalPropertySliderOverflow');
			popup.addClass('open');
			
			popup.click(self.popupClose);
		}
		
		this.popupClose		= function() {
			popup.removeClass('open');
			$(document.body).removeClass('ancapitalPropertySliderOverflow');
		}
		
		
		
		// Инициализация
		
		this.refresh();
	}
	
	// Инициализация Слайдера

	$(function() {
		$('.ancapitalPropertySlider').ancapitalPropertySlider()
	})
	
})(jQuery)