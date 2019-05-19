var menu = [
  {
    name: "test1",
    img_src: "https://image.flaticon.com/icons/svg/1046/1046784.svg"
  },
  {
    name: "test2",
    img_src: "https://image.flaticon.com/icons/svg/1046/1046784.svg"
  },
  {
    name: "test3",
    img_src: "https://image.flaticon.com/icons/svg/1046/1046784.svg"
  },
  {
    name: "test4",
    img_src: "https://image.flaticon.com/icons/svg/1046/1046784.svg"
  },
  {
    name: "test5",
    img_src: "https://image.flaticon.com/icons/svg/1046/1046784.svg"
  }
];

var flexCss = {
  display: "flex",
  "justify-content": "center",
  "align-items": "center"
};

function introFadeIn() {
  $("#intro").fadeIn("slow");
  $("#intro").css(flexCss);
}

function loadFadeIn() {
  $("#intro").fadeOut("slow");
  $("#load").fadeIn("slow");
  $("#load").css(flexCss);
}

function mainFadeIn() {
  $("#load").fadeOut("slow");
  $("#main").fadeIn("slow");
  toggleMainContent();
}

function toggleMainContent() {
  menu.map(e => {
    $(".grid").append(`
      <div class="item">
        <div class="item-content">
          <img src="${e.img_src}" style="width: 60px; margin: auto;">
          <p>${e.name}</p>
        </div>
      </div>
    `);
  });

  var grid = new Muuri(".grid", { dragEnabled: true });

  $(".carousel").slick({
    slidesToShow: 1,
    slidesToScroll: 1,
    autoplay: true,
    autoplaySpeed: 2000,
    arrows: false
    // dots: true
  });
}

$(document).ready(function() {
  introFadeIn();

  setTimeout(loadFadeIn, 2000);
  setTimeout(mainFadeIn, 4000);
});
