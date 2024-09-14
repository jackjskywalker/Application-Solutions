// script.js

function calculateEarnings() {
    try {
        let inputs = [
            { id: 'earning-goal', min: 0, max: Infinity, message: 'Earning goal must be a positive number' },
            { id: 'sales-commission', min: 0, max: 100, message: 'Sales commission must be a percentage value between 0 and 100' },
            { id: 'average-contract-value', min: 0, max: Infinity, message: 'Average contract value must be a positive number' }
        ];

        let values = {};
        for (let input of inputs) {
            let value = parseFloat(document.getElementById(input.id).value);
            if (isNaN(value) || value < input.min || value > input.max) {
                throw new Error(input.message);
            }
            values[input.id] = value;
        }

        let startDate = new Date(document.getElementById('start-date').value);
        let endDate = new Date(document.getElementById('end-date').value);
        let dayOff = document.getElementById('day-off').value;

        // Validate the dates
        if (isNaN(startDate.getTime()) || isNaN(endDate.getTime())) {
            throw new Error('Invalid date format. Please use YYYY-MM-DD.');
        }

        // Calculate the total work days
        let totalDays = 0;
        for (let date = startDate; date <= endDate; date.setDate(date.getDate() + 1)) {
            if (date.getDay() != dayOff) {
                totalDays++;
            }
        }

        // Add one day to the total days if the end date is not a day off
        if (endDate.getDay() != dayOff) {
            totalDays++;
        }

        // Calculate the total revenue needed to hit the goal
        let totalRevenue = values['earning-goal'] / (values['sales-commission'] / 100);

        // Calculate the number of sales per day and week
        let salesPerDay = totalRevenue / values['average-contract-value'] / totalDays;
        let salesPerWeek = salesPerDay * 7;

        // Calculate the number of sales needed
        let salesNeeded = totalRevenue / values['average-contract-value'];

        // Display the results
        let result = document.getElementById('result');
        result.innerHTML = `
            <h2>Results</h2>
            <p>Total days: ${totalDays}</p>
            <p>Sales per day: ${salesPerDay.toFixed(2)}</p>
            <p>Sales per week: ${salesPerWeek.toFixed(2)}</p>
            <p>Total sales needed: ${salesNeeded.toFixed(2)}</p>
            <p>Total revenue needed: $${totalRevenue.toLocaleString(undefined, {minimumFractionDigits: 2, maximumFractionDigits: 2})}</p>
        `;
    } catch (error) {
        let result = document.getElementById('result');
        result.innerHTML = `
            <h2>Error</h2>
            <p>${error.message}</p>
        `;
    }
}

function saveResults() {
    let earningGoal = document.getElementById('earning-goal').value;
    let salesCommission = document.getElementById('sales-commission').value;
    let averageContractValue = document.getElementById('average-contract-value').value;
    let startDate = document.getElementById('start-date').value;
    let endDate = document.getElementById('end-date').value;
    let result = document.getElementById('result');
    let text = `Results for $${earningGoal} Sales Goal:

    Earning Goal: $${earningGoal}
    Sales Commission: ${salesCommission}%
    Average Contract Value: $${averageContractValue}
    Start Date: ${startDate}
    End Date: ${endDate}

    Total work days: ${result.children[1].textContent.replace('Total work days: ', '')}
    Sales per day: ${result.children[2].textContent.replace('Sales per day: ', '')}
    Sales per week: ${result.children[3].textContent.replace('Sales per week: ', '')}
    Total sales needed: ${result.children[4].textContent.replace('Total sales needed: ', '')}
    Revenue needed: ${result.children[5].textContent.replace('Revenue needed: ', '')}`;

    let blob = new Blob([text], {type: 'text/plain'});
    let link = document.createElement('a');
    link.href = URL.createObjectURL(blob);
    link.download = `SalesEarnings.txt`;
    link.click();
}