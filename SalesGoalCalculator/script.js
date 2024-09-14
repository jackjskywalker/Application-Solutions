// script.js

function toggleGoalInput() {
    let goalType = document.getElementById('goal-type').value;
    let salesPerDayInput = document.getElementById('sales-per-day');
    let salesPerWeekInput = document.getElementById('sales-per-week');
    if (goalType === 'day') {
        salesPerDayInput.disabled = false;
        salesPerWeekInput.disabled = true;
    } else {
        salesPerDayInput.disabled = true;
        salesPerWeekInput.disabled = false;
    }
}

function calculateEarnings() {
    try {
        let goalType = document.getElementById('goal-type').value;
        let inputs = [
            { id: 'sales-commission', min: 0, max: 100, message: 'Sales commission must be a percentage value between 0 and 100' },
            { id: 'average-contract-value', min: 0, max: Infinity, message: 'Average contract value must be a positive number' }
        ];
        if (goalType === 'day') {
            inputs.push({ id: 'sales-per-day', min: 0, max: Infinity, message: 'Sales per day must be a positive number' });
        } else {
            inputs.push({ id: 'sales-per-week', min: 0, max: Infinity, message: 'Sales per week must be a positive number' });
        }

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

        // Calculate the total sales
        let totalSales;
        if (goalType === 'day') {
            totalSales = values['sales-per-day'] * totalDays;
        } else {
            totalSales = values['sales-per-week'] * (totalDays / 7);
        }

        // Calculate the total revenue
        let totalRevenue = totalSales * values['average-contract-value'];

        // Calculate the total earnings
        let totalEarnings = totalRevenue * (values['sales-commission'] / 100);

        // Display the results
        let result = document.getElementById('result');
        result.innerHTML = `
            <h2>Results</h2>
            <p>Total days: ${totalDays}</p>
            <p>Total sales: ${totalSales.toFixed(2)}</p>
            <p>Total revenue: $${totalRevenue.toLocaleString(undefined, {minimumFractionDigits: 2, maximumFractionDigits: 2})}</p>
            <p>Total earnings: $${totalEarnings.toLocaleString(undefined, {minimumFractionDigits: 2, maximumFractionDigits: 2})}</p>
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
    let goalType = document.getElementById('goal-type').value;
    let salesPerDay = document.getElementById('sales-per-day').value;
    let salesPerWeek = document.getElementById('sales-per-week').value;
    let salesCommission = document.getElementById('sales-commission').value;
    let averageContractValue = document.getElementById('average-contract-value').value;
    let startDate = document.getElementById('start-date').value;
    let endDate = document.getElementById('end-date').value;
    let result = document.getElementById('result');
    let text = `Results for:

    Goal type: ${goalType === 'day' ? 'Sales per day' : 'Sales per week'}
    ${goalType === 'day' ? 'Sales per day: ' + salesPerDay : 'Sales per week: ' + salesPerWeek}
    Sales commission: ${salesCommission}%
    Average contract value: $${averageContractValue}
    Start date: ${startDate}
    End date: ${endDate}

    Total work days: ${result.children[1].textContent.replace('Total work days: ', '')}
    Total number of sales: ${result.children[2].textContent.replace('Total number of sales: ', '')}
    Total revenue: ${result.children[3].textContent.replace('Total revenue: ', '')}
    Total earnings: ${result.children[4].textContent.replace('Total earnings: ', '')}`;

    let blob = new Blob([text], {type: 'text/plain'});
    let link = document.createElement('a');
    link.href = URL.createObjectURL(blob);
    link.download = `SalesGoal.txt`;
    link.click();
}