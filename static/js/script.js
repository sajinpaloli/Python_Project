document.addEventListener("DOMContentLoaded", function () {
    const updateDashboard = () => {
        fetch("/api/data", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({}),
        })
            .then((res) => res.json())
            .then((data) => {
                
                document.getElementById("avg-exam-score").textContent = data.avg_exam_score;
                document.getElementById("avg-study-hours").textContent = data.avg_study_hours;
                document.getElementById("avg-attendance").textContent = data.avg_attendance;

                
                updateGenderDistributionChart(data.gender_distribution);
                updateSchoolTypeChart(data.school_type_distribution);
            });
    };

    const updateGenderDistributionChart = (data) => {
        const ctx = document.getElementById("gender-distribution-chart").getContext("2d");
        new Chart(ctx, {
            type: "pie",
            data: {
                labels: Object.keys(data),
                datasets: [
                    {
                        data: Object.values(data),
                        backgroundColor: ["#FF6384", "#36A2EB"],
                    },
                ],
            },
            options: {
                responsive: false,
            },
        });
    };

    const updateSchoolTypeChart = (data) => {
        const ctx = document.getElementById("school-type-chart").getContext("2d");
        new Chart(ctx, {
            type: "bar",
            data: {
                labels: Object.keys(data),
                datasets: [
                    {
                        label: "School Type Distribution",
                        data: Object.values(data),
                        backgroundColor: ["#4BC0C0", "#FFCE56"],
                    },
                ],
            },
        });
    };

    updateDashboard();
});
