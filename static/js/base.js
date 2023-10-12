$(document).ready(function () {
        $(".dropdown_btn").click(function () {
            $(".slidedown").slideToggle("slow");
        });
    });

    $(document).ready(function () {
        $(".button_dropdown").click(function () {
            $(".slidedown_gallery").slideToggle("slow");
        });
    });

     $('.btt-link').click(function (e) {
        window.scrollTo(0, 0)
    })

     $('#sort-selector').change(function () {
        var selector = $(this);
        var currentUrl = new URL(window.location);

        var selectedVal = selector.val();
        if (selectedVal != "reset") {
            var sort = selectedVal.split("_")[0];
            var direction = selectedVal.split("_")[1];

            currentUrl.searchParams.set("sort", sort);
            currentUrl.searchParams.set("direction", direction);

            window.location.replace(currentUrl);
        } else {
            currentUrl.searchParams.delete("sort");
            currentUrl.searchParams.delete("direction");

            window.location.replace(currentUrl);
        }
    })

      // Update quantity on click
    $('.update-link').click(function (e) {
        var form = $(this).prev('.update-form');
        form.submit();
    })

    // Remove item and reload on click
    $('.remove-item').click(function (e) {
        var csrfToken = "{{ csrf_token }}";
        var itemId = $(this).attr('id').split('remove_')[1];
        var url = `/bag/remove/${itemId}`;

        $.post(url, data)
            .done(function () {
                location.reload();
            });
    })