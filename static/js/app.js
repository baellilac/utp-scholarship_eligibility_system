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
                    <span>Overall Eligibility Probability</span>
                    <span>${probability.toFixed(1)}%</span>
                </div>
                <div class="probability-bar-container">
                    <div class="probability-bar-fill" style="width: ${probability}%">
                        ${probability.toFixed(1)}%
                    </div>
                </div>
            </div>
        </div>
    `;
    
    // Display specific scholarship recommendations
    if (data.scholarship_recommendations && data.scholarship_recommendations.length > 0) {
        html += `
            <div style="margin-top: 30px; padding-top: 20px; border-top: 2px solid rgba(255,255,255,0.3);">
                <h3 style="margin-bottom: 20px; font-size: 1.3rem;">🎓 Specific Scholarship Recommendations</h3>
                <p style="margin-bottom: 15px; opacity: 0.9;">
                    Based on your profile, here are your eligibility status for specific scholarship providers:
                </p>
                <div style="display: grid; gap: 15px;">
        `;
        
        data.scholarship_recommendations.forEach(scholarship => {
            const eligible = scholarship.eligible;
            const bgColor = eligible ? 'rgba(16, 185, 129, 0.2)' : 'rgba(239, 68, 68, 0.2)';
            const borderColor = eligible ? 'rgba(16, 185, 129, 0.5)' : 'rgba(239, 68, 68, 0.5)';
            
            html += `
                <div style="background: ${bgColor}; border: 2px solid ${borderColor}; padding: 15px; border-radius: 10px;">
                    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 10px;">
                        <h4 style="margin: 0; font-size: 1.1rem;">
                            ${eligible ? '✅' : '❌'} ${scholarship.name}
                        </h4>
                        <span style="background: ${eligible ? 'rgba(16, 185, 129, 0.3)' : 'rgba(239, 68, 68, 0.3)'}; 
                                     padding: 4px 12px; border-radius: 12px; font-size: 0.85rem; font-weight: bold;">
                            ${eligible ? 'ELIGIBLE' : 'NOT ELIGIBLE'}
                        </span>
                    </div>
                    <p style="margin: 8px 0; font-size: 0.9rem; opacity: 0.9;">
                        ${scholarship.description}
                    </p>
                    <div style="margin-top: 10px;">
                        <strong style="font-size: 0.9rem;">${eligible ? 'Why you qualify:' : 'What you need to improve:'}</strong>
                        <ul style="margin: 8px 0; padding-left: 20px; font-size: 0.85rem;">
            `;
            
            scholarship.reasons.forEach(reason => {
                html += `<li style="margin: 4px 0;">${reason}</li>`;
            });
            
            html += `
                        </ul>
                    </div>
                </div>
            `;
        });
        
        html += `
                </div>
                <div style="margin-top: 15px; padding: 12px; background: rgba(59, 130, 246, 0.2); border-radius: 8px; border-left: 4px solid #3b82f6;">
                    <strong>📊 Summary:</strong> You are eligible for <strong>${data.eligible_scholarships_count} out of ${data.scholarship_recommendations.length}</strong> scholarship providers.
                    ${data.eligible_scholarships_count > 0 ? 
                        `<br>Recommended scholarships: <strong>${data.eligible_scholarships.join(', ')}</strong>` : 
                        '<br>Consider improving your profile to meet scholarship criteria.'}
                </div>
            </div>
        `;
    }
    
    // Display model predictions with explanations
    html += `
        <div style="margin-top: 30px; padding-top: 20px; border-top: 2px solid rgba(255,255,255,0.3);">
            <h3 style="margin-bottom: 15px; font-size: 1.3rem;">🤖 AI Model Predictions Explained</h3>
            <p style="margin-bottom: 15px; opacity: 0.9; font-size: 0.95rem;">
                Our system uses 3 different AI models to analyze your profile. Each model has its own approach:
            </p>
            <div style="display: grid; gap: 12px;">
    `;
    
    if (data.all_predictions && data.all_probabilities && data.model_explanations) {
        for (const [modelName, prediction] of Object.entries(data.all_predictions)) {
            const prob = data.all_probabilities[modelName];
            const explanation = data.model_explanations[modelName];
            const isPrimary = modelName === data.model_used;
            
            if (prob && explanation) {
                const modelEligible = prediction === 1;
                const modelProb = ((prob.eligible || 0) * 100).toFixed(1);
                
                html += `
                    <div style="background: rgba(255,255,255,${isPrimary ? '0.25' : '0.15'}); 
                                padding: 15px; border-radius: 8px; 
                                border-left: 4px solid ${isPrimary ? '#10b981' : 'rgba(255,255,255,0.5)'};">
                        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 10px;">
                            <div>
                                <strong style="font-size: 1rem;">${modelName}</strong>
                                ${isPrimary ? '<span style="background: rgba(16, 185, 129, 0.3); padding: 2px 8px; border-radius: 8px; font-size: 0.75rem; margin-left: 8px;">PRIMARY MODEL</span>' : ''}
                            </div>
                            <div style="text-align: right;">
                                <div style="font-size: 1.1rem; font-weight: bold;">
                                    ${modelEligible ? '✅ Eligible' : '❌ Not Eligible'}
                                </div>
                                <div style="font-size: 0.85rem; opacity: 0.8;">
                                    ${modelProb}% confidence
                                </div>
                            </div>
                        </div>
                        <div style="margin-top: 10px; padding-top: 10px; border-top: 1px solid rgba(255,255,255,0.2);">
                            <p style="font-size: 0.9rem; margin: 5px 0; opacity: 0.9;">
                                <strong>How it works:</strong> ${explanation.description}
                            </p>
                            <p style="font-size: 0.85rem; margin: 5px 0; opacity: 0.8;">
                                <strong>Strength:</strong> ${explanation.strength}
                            </p>
                            <p style="font-size: 0.85rem; margin: 5px 0; opacity: 0.8;">
                                <strong>Use case:</strong> ${explanation.use_case}
                            </p>
                        </div>
                    </div>
                `;
            }
        }
    }
    
    html += `
            </div>
            <div style="margin-top: 15px; padding: 12px; background: rgba(139, 92, 246, 0.2); border-radius: 8px; border-left: 4px solid #8b5cf6;">
                <strong>💡 Understanding the Results:</strong> 
                <ul style="margin: 8px 0; padding-left: 20px; font-size: 0.9rem;">
                    <li><strong>Logistic Regression</strong> gives you a baseline prediction using statistical patterns</li>
                    <li><strong>Decision Tree</strong> shows you the specific rules and criteria used in the decision</li>
                    <li><strong>Random Forest</strong> (primary model) combines multiple decision trees for the most accurate prediction</li>
                </ul>
                <p style="margin-top: 8px; font-size: 0.85rem; opacity: 0.9;">
                    The final recommendation is based on the <strong>${data.model_used}</strong> model, which is our most reliable predictor.
                </p>
            </div>
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

