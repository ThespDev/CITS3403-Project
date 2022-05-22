// Creating the collapsible sidebar for guesses

$(window).on('load', () => {
  
    // Initialising required constants
    const overlay_div = document.getElementById('overlay')
    const overlay_txt = document.getElementById('overlay-text')
  
    const share_div = document.getElementById('share')
    const share_txt = document.getElementById('share-text')
  
    const thanks_div = document.getElementById('thanks')
    const thanks_txt = document.getElementById('thanks-text')
  
    const web_button = document.getElementById('share-site')
  
    const themes_div = document.getElementById('themes');
    const themes_txt = document.getElementById('themes-text');
  
    const base_theme = document.getElementById('base-theme')
    const cameron_theme = document.getElementById('cameron-theme')
    const maaz_theme = document.getElementById('maaz-theme')
  
    
  
    // Code blocks to stop the div from disappearing when clicking in the text field, but to disappear when clicking outside the field.
    share_div.addEventListener("click", function() {
      $('#share').fadeOut(100);
    }, false);
    share_txt.addEventListener("click", function(ev) {
      ev.stopPropagation();
    }, false);
  
    $(overlay_div).click(function() {
      $('#overlay').fadeOut(100)
    })
    overlay_txt.addEventListener("click", function(ev) {
      ev.stopPropagation();
    }, false);
  
    $(thanks_div).click(function() {
      $('#thanks').fadeOut(100)
    })
    thanks_txt.addEventListener("click", function(ev) {
      ev.stopPropagation();
    }, false);
  
    themes_div.addEventListener("click", function() {
      $('#themes').fadeOut(100);
    }, false);
  
    themes_txt.addEventListener("click", function(ev) {
      ev.stopPropagation();
    }, false);
  
    const current_theme = document.getElementById('background')
  
    base_theme.addEventListener('click', function() {
      current_theme.className = base_theme.id
    });
  
    maaz_theme.addEventListener('click', function() {
      current_theme.className = maaz_theme.id
    });
  
    cameron_theme.addEventListener('click', function() {
      current_theme.className = cameron_theme.id
    });
  
    if (current_theme.className === 'base_theme') {
      base_theme.innerHTML = 'Selected!'
    } else {
      base_theme.innerHTML = 'Base Theme'
    }
  
    if (current_theme.className === 'cameron_theme') {
      cameron_theme.innerHTML = 'Selected!'
    } else {
      cameron_theme.innerHTML = 'Cameron Theme'
    }
  
    if (current_theme.className === 'maaz_theme') {
      maaz_theme.innerHTML = 'Selected!'
    } else {
      maaz_theme.innerHTML = 'Maaz Theme'
    }
  
    web_button.addEventListener('click', function() {
      web_button.innerHTML = "Copied to Clipboard!";
      navigator.clipboard.writeText(window.location.href)
    });

    $('.message a').click(function(){
        $('form').animate({height: "toggle", opacity: "toggle"}, "slow");
      });
  
  });
  
  // Function to turn on the overlays when buttons at the top are clicked (Or when the user runs out of guesses/gets the correct answer.)
  function onRules() {
    document.getElementById("overlay").className = 'fade-in';
    document.getElementById("overlay").style.display = "block";
  }
  
  function onShare() {
    document.getElementById("share").className = 'fade-in';
    document.getElementById("share").style.display = "block";
  }
  
  function onThanks() {
    document.getElementById("thanks").className = 'fade-in';
    document.getElementById("thanks").style.display = "block";
  }
  
  function onThemes() {
    document.getElementById("themes").className = 'fade-in';
    document.getElementById("themes").style.display = "block";
  }
  