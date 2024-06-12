var navbar = document.getElementById("present-nav-bar");
var test_id = document.querySelectorAll(".present-just-nav-bar")
var brandLogo = document.getElementById("present-page-nav-bar-brand-logo");
var Sm_Line = document.getElementById("present-page-a-bareek-line-below-nav-bar");
var linediv = document.getElementById("ohoo");

        window.addEventListener("scroll", function() {
            var scrollY = window.scrollY;

            if (scrollY < 700)
               {
                navbar.style.backgroundColor = "transparent";
                test_id.forEach(function(elem)
                {
                    elem.style.color="white";
                });
                navbar.style.animation="hide-towards-top 0.7s ease-in";
                linediv.style.backgroundColor="transparent";
                brandLogo.src="static/img3/DEVWITHOPS-1.png";
                Sm_Line.style.opacity=0;
                }
                else 
                {
                    navbar.style.backgroundColor = "white";
                    test_id.forEach(function(elem)
                    {
                        elem.style.color="black";
                        
                    });
                    navbar.style.backgroundColor="white";
                    navbar.style.animation="appear-from-top 0.7s ease-in";
                    linediv.style.backgroundColor="white";
                    brandLogo.src="static/img3/devops.png";
                    Sm_Line.style.opacity=1;
                }
        });