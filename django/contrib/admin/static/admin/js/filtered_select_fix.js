(function($) {
    $(document).ready(function() {
        // Function to reinitialize FilteredSelectMultiple widgets
        function reinitializeFilteredSelectMultiple() {
            $(".filtered").each(function() {
                const $this = $(this);
                const id = $this.attr("id");

                // Check if SelectFilter is already initialized
                if (!$this.data("selectfilter-initialized")) {
                    SelectFilter.init(id, $this.attr("data-field-name"), false);
                    $this.data("selectfilter-initialized", true);
                }
            });
        }

        // Reinitialize on inline formset removal
        $(document).on("formset:removed", function() {
            reinitializeFilteredSelectMultiple();
        });

        // Initial setup on page load
        reinitializeFilteredSelectMultiple();
    });
})(django.jQuery);
