// Tab switching
function showTab(tabName) {
    // Hide all tabs
    document.querySelectorAll('.tab-content').forEach(tab => {
        tab.classList.remove('active');
    });
    
    // Remove active class from all buttons
    document.querySelectorAll('.tab-btn').forEach(btn => {
        btn.classList.remove('active');
    });
    
    // Show selected tab
    document.getElementById(`${tabName}-tab`).classList.add('active');
    
    // Add active class to clicked button
    event.target.classList.add('active');
    
    // Load data for dashboard and models tabs
    if (tabName === 'dashboard') {
        loadDashboard();
    } else if (tabName === 'models') {
        loadModelPerformance();
    }
}

// Prediction form handler
document.getElementById('prediction-form').addEventListener('submit', async (e) => {
    e.preventDefault();
    
    const formData = {
        year_of_study: parseInt(document.getElementById('year_of_study').value),
        cgpa: parseFloat(document.getElementById('cgpa').value),
        family_income: parseInt(document.getElementById('family_income').value),
        cocurricular_score: parseInt(document.getElementById('cocurricular_score').value),
        leadership_positions: parseInt(document.getElementById('leadership_positions').value),
        community_service_hours: parseInt(document.getElementById('community_service_hours').value)
    };
    
    try {
        const response = await fetch('/predict', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(formData)
        });
        
        const data = await response.json();
        
        if (data.success) {
            displayPredictionResult(data);
        } else {
            showError(data.error || 'An error occurred while processing your request.');
        }
    } catch (error) {
        console.error('Error:', error);
        showError('An error occurred. Please try again. Error: ' + error.message);
    }
});

// Display prediction result
function displayPredictionResult(data) {
    const resultContainer = document.getElementById('prediction-result');
    const resultContent = document.getElementById('result-content');
    
    // Check if data has required fields
    if (!data || data.prediction === undefined || !data.probability) {
        showError('Invalid response from server. Please try again.');
        return;
    }
    
    const isEligible = data.prediction === 1;
    const probability = (data.probability.eligible || 0) * 100;
    
    resultContainer.className = `result-container ${isEligible ? 'result-eligible' : 'result-not-eligible'}`;
    
    let html = `
        <div style="text-align: center; margin-bottom: 20px;">
            <h2 style="font-size: 2rem; margin-bottom: 10px;">
                ${isEligible ? '✅ Eligible' : '❌ Not Eligible'}
            </h2>
            <p style="font-size: 1.1rem; opacity: 0.9;">
                ${isEligible ? 'Congratulations! You are eligible for scholarships.' : 'You may not meet the current eligibility criteria.'}
            </p>
        </div>
        
        <div class="probability-bar">
            <div class="probability-item">
                <div class="probability-label">
                    <span>Eligibility Probability</span>
                    <span>${probability.toFixed(1)}%</span>
                </div>
                <div class="probability-bar-container">
                    <div class="probability-bar-fill" style="width: ${probability}%">
                        ${probability.toFixed(1)}%
                    </div>
                </div>
            </div>
        </div>
        
        <div style="margin-top: 25px; padding-top: 20px; border-top: 2px solid rgba(255,255,255,0.3);">
            <h4 style="margin-bottom: 15px;">Model Predictions:</h4>
            <div style="display: grid; gap: 10px;">
    `;
    
    if (data.all_predictions && data.all_probabilities) {
        for (const [modelName, prediction] of Object.entries(data.all_predictions)) {
            const prob = data.all_probabilities[modelName];
            if (prob) {
                const modelEligible = prediction === 1;
                html += `
                    <div style="background: rgba(255,255,255,0.2); padding: 12px; border-radius: 8px;">
                        <div style="display: flex; justify-content: space-between; align-items: center;">
                            <span><strong>${modelName}:</strong> ${modelEligible ? '✅ Eligible' : '❌ Not Eligible'}</span>
                            <span>${((prob.eligible || 0) * 100).toFixed(1)}%</span>
                        </div>
                    </div>
                `;
            }
        }
    }
    
    html += `
            </div>
            <p style="margin-top: 15px; font-size: 0.9rem; opacity: 0.8;">
                Primary Model: <strong>${data.model_used}</strong>
            </p>
        </div>
    `;
    
    resultContent.innerHTML = html;
    resultContainer.style.display = 'block';
    
    // Scroll to result
    resultContainer.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
}

// Load dashboard data
async function loadDashboard() {
    try {
        const response = await fetch('/dataset_stats');
        const data = await response.json();
        
        if (data.success) {
            const stats = data.stats;
            
            // Update stat cards
            document.getElementById('total-students').textContent = stats.total_samples;
            document.getElementById('eligible-count').textContent = stats.eligible_count;
            document.getElementById('not-eligible-count').textContent = stats.not_eligible_count;
            document.getElementById('eligibility-rate').textContent = stats.eligible_percentage.toFixed(1) + '%';
            
            // Create charts
            createEligibilityChart(stats);
            createCGPAChart(stats);
            createIncomeChart(stats);
        }
    } catch (error) {
        console.error('Error loading dashboard:', error);
    }
}

// Create eligibility pie chart
function createEligibilityChart(stats) {
    const ctx = document.getElementById('eligibilityChart').getContext('2d');
    
    if (window.eligibilityChartInstance) {
        window.eligibilityChartInstance.destroy();
    }
    
    window.eligibilityChartInstance = new Chart(ctx, {
        type: 'doughnut',
        data: {
            labels: ['Eligible', 'Not Eligible'],
            datasets: [{
                data: [stats.eligible_count, stats.not_eligible_count],
                backgroundColor: ['#10b981', '#ef4444'],
                borderWidth: 2,
                borderColor: '#ffffff'
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: true,
            plugins: {
                title: {
                    display: true,
                    text: 'Scholarship Eligibility Distribution',
                    font: { size: 18, weight: 'bold' }
                },
                legend: {
                    position: 'bottom'
                }
            }
        }
    });
}

// Create CGPA distribution chart
function createCGPAChart(stats) {
    const ctx = document.getElementById('cgpaChart').getContext('2d');
    
    if (window.cgpaChartInstance) {
        window.cgpaChartInstance.destroy();
    }
    
    // Simulate CGPA distribution (in real app, this would come from backend)
    const cgpaRanges = ['2.0-2.5', '2.5-3.0', '3.0-3.5', '3.5-4.0'];
    const distribution = [150, 400, 800, 650]; // Sample data
    
    window.cgpaChartInstance = new Chart(ctx, {
        type: 'bar',
        data: {
            labels: cgpaRanges,
            datasets: [{
                label: 'Number of Students',
                data: distribution,
                backgroundColor: '#2563eb',
                borderRadius: 8
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: true,
            plugins: {
                title: {
                    display: true,
                    text: 'CGPA Distribution',
                    font: { size: 18, weight: 'bold' }
                },
                legend: {
                    display: false
                }
            },
            scales: {
                y: {
                    beginAtZero: true
                }
            }
        }
    });
}

// Create income distribution chart
function createIncomeChart(stats) {
    const ctx = document.getElementById('incomeChart').getContext('2d');
    
    if (window.incomeChartInstance) {
        window.incomeChartInstance.destroy();
    }
    
    // Simulate income distribution
    const incomeRanges = ['0-30k', '30k-60k', '60k-90k', '90k-120k', '120k+'];
    const distribution = [400, 500, 450, 350, 300]; // Sample data
    
    window.incomeChartInstance = new Chart(ctx, {
        type: 'bar',
        data: {
            labels: incomeRanges,
            datasets: [{
                label: 'Number of Students',
                data: distribution,
                backgroundColor: '#8b5cf6',
                borderRadius: 8
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: true,
            plugins: {
                title: {
                    display: true,
                    text: 'Family Income Distribution (RM)',
                    font: { size: 18, weight: 'bold' }
                },
                legend: {
                    display: false
                }
            },
            scales: {
                y: {
                    beginAtZero: true
                }
            }
        }
    });
}

// Load model performance
async function loadModelPerformance() {
    try {
        const response = await fetch('/model_info');
        const data = await response.json();
        
        if (data.success) {
            displayModelComparison(data.results);
            createModelMetricsChart(data.results);
        } else {
            document.getElementById('model-comparison').innerHTML = 
                '<div class="error">Model results not available. Please train models first.</div>';
        }
    } catch (error) {
        console.error('Error loading model performance:', error);
        document.getElementById('model-comparison').innerHTML = 
            '<div class="error">Error loading model performance data.</div>';
    }
}

// Display model comparison
function displayModelComparison(results) {
    const container = document.getElementById('model-comparison');
    let html = '';
    
    for (const [modelName, metrics] of Object.entries(results)) {
        html += `
            <div class="model-card">
                <h3>${modelName}</h3>
                <div class="metrics-grid">
                    <div class="metric-item">
                        <div class="metric-label">Accuracy</div>
                        <div class="metric-value">${(metrics.accuracy * 100).toFixed(2)}%</div>
                    </div>
                    <div class="metric-item">
                        <div class="metric-label">Precision</div>
                        <div class="metric-value">${(metrics.precision * 100).toFixed(2)}%</div>
                    </div>
                    <div class="metric-item">
                        <div class="metric-label">Recall</div>
                        <div class="metric-value">${(metrics.recall * 100).toFixed(2)}%</div>
                    </div>
                    <div class="metric-item">
                        <div class="metric-label">F1-Score</div>
                        <div class="metric-value">${(metrics.f1_score * 100).toFixed(2)}%</div>
                    </div>
                </div>
            </div>
        `;
    }
    
    container.innerHTML = html;
}

// Create model metrics comparison chart
function createModelMetricsChart(results) {
    const ctx = document.getElementById('modelMetricsChart').getContext('2d');
    
    if (window.modelMetricsChartInstance) {
        window.modelMetricsChartInstance.destroy();
    }
    
    const modelNames = Object.keys(results);
    const metrics = ['accuracy', 'precision', 'recall', 'f1_score'];
    const metricLabels = ['Accuracy', 'Precision', 'Recall', 'F1-Score'];
    
    const datasets = modelNames.map((name, index) => {
        const colors = ['#2563eb', '#10b981', '#f59e0b'];
        return {
            label: name,
            data: metrics.map(metric => results[name][metric] * 100),
            backgroundColor: colors[index % colors.length],
            borderRadius: 8
        };
    });
    
    window.modelMetricsChartInstance = new Chart(ctx, {
        type: 'bar',
        data: {
            labels: metricLabels,
            datasets: datasets
        },
        options: {
            responsive: true,
            maintainAspectRatio: true,
            plugins: {
                title: {
                    display: true,
                    text: 'Model Performance Comparison',
                    font: { size: 18, weight: 'bold' }
                },
                legend: {
                    position: 'top'
                }
            },
            scales: {
                y: {
                    beginAtZero: true,
                    max: 100,
                    ticks: {
                        callback: function(value) {
                            return value + '%';
                        }
                    }
                }
            }
        }
    });
}

// Show error message
function showError(message) {
    const resultContainer = document.getElementById('prediction-result');
    const resultContent = document.getElementById('result-content');
    
    resultContainer.className = 'result-container error';
    resultContent.innerHTML = `<p>${message}</p>`;
    resultContainer.style.display = 'block';
}

// Initialize dashboard on page load if on dashboard tab
document.addEventListener('DOMContentLoaded', () => {
    // Check if dashboard tab is active
    if (document.getElementById('dashboard-tab').classList.contains('active')) {
        loadDashboard();
    }
});

