$(document).ready(function () {
    $("#my-team-btn").click(function (e) {
        e.preventDefault();
        $("#team-sidebar").toggle(); // Show/Hide the secondary sidebar

        // Fetch departments if they haven't been loaded yet
        if ($("#department-select option").length === 1) {
            $.ajax({
                url: "/get-departments/",
                method: "GET",
                success: function (data) {
                    data.departments.forEach(function (dept) {
                        $("#department-select").append(`<option value="${dept.id}">${dept.name}</option>`);
                    });
                },
                error: function () {
                    alert("Failed to load departments.");
                }
            });
        }
    });

    // Load employees when a department is selected
    $("#department-select").change(function () {
        let departmentId = $(this).val();
        if (departmentId) {
            $.ajax({
                url: `/get-employees/${departmentId}/`,
                method: "GET",
                success: function (data) {
                    let teamList = $("#team-list");
                    teamList.empty(); // Clear old list
                    data.employees.forEach(function (emp) {
                        teamList.append(`<li>${emp.name} - ${emp.position}</li>`);
                    });
                },
                error: function () {
                    alert("Failed to load team members.");
                }
            });
        } else {
            $("#team-list").empty();
        }
    });
});
