var date_range = null;
var date_now = new moment().format("YYYY-MM-DD");



$(function () {
  $('input[name="date_range"]')
    .daterangepicker({
      locale: {
        format: "YYYY-MM-DD",
        applyLabel: '<i class="fas fa-chart-pie"></i> Aplicar',
        cancelLabel: '<i class="fas fa-times"></i> Cancelar',
      },
    })
    .on("apply.daterangepicker", function (ev, picker) {
      date_range = picker;
      console.log(date_range.endDate);
    })
    .on("cancel.daterangepicker", function (ev, picker) {
      $(this).data("daterangepicker").setStartDate(date_now);
      $(this).data("daterangepicker").setEndDate(date_now);
      date_range = picker;
      console.log(date_range.endDate);
    });
});
