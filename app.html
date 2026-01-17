<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
    <meta name="theme-color" content="#16a085">
    <meta name="apple-mobile-web-app-capable" content="yes">
    <meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">
    <meta name="apple-mobile-web-app-title" content="CareAide">
    <meta name="description" content="Eldercare Reminder App - Never miss medications, appointments, or daily health tasks">
    
    <!-- PWA Manifest -->
    <link rel="manifest" href="data:application/json,%7B%22name%22%3A%22CareAide%20Eldercare%20App%22%2C%22short_name%22%3A%22CareAide%22%2C%22description%22%3A%22Eldercare%20Reminder%20App%22%2C%22start_url%22%3A%22.%22%2C%22display%22%3A%22standalone%22%2C%22background_color%22%3A%22%2316a085%22%2C%22theme_color%22%3A%22%2316a085%22%2C%22icons%22%3A%5B%7B%22src%22%3A%22data%3Aimage%2Fsvg%2Bxml%2C%253Csvg%2520xmlns%3D%27http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%27%2520viewBox%3D%270%25200%2520100%2520100%27%253E%253Crect%2520fill%3D%27%252316a085%27%2520width%3D%27100%27%2520height%3D%27100%27%2520rx%3D%2720%27%2F%253E%253Ctext%2520x%3D%2750%27%2520y%3D%2765%27%2520font-size%3D%2750%27%2520text-anchor%3D%27middle%27%253E%25F0%259F%2592%258A%253C%2Ftext%253E%253C%2Fsvg%253E%22%2C%22sizes%22%3A%22512x512%22%2C%22type%22%3A%22image%2Fsvg%2Bxml%22%7D%5D%7D">
    
    <!-- iOS Icons -->
    <link rel="apple-touch-icon" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'><rect fill='%2316a085' width='100' height='100' rx='20'/><text x='50' y='65' font-size='50' text-anchor='middle'>💊</text></svg>">
    
    <title>CareAide - Eldercare Reminder App</title>
    <script src="https://cdn.jsdelivr.net/npm/@tailwindcss/browser@4"></script>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');
        
        * { 
            font-family: 'Inter', sans-serif; 
            -webkit-tap-highlight-color: transparent;
            box-sizing: border-box;
        }
        
        html, body {
            overscroll-behavior: none;
            -webkit-overflow-scrolling: touch;
        }
        
        :root {
            --primary: #16a085;
            --primary-dark: #138a72;
            --danger: #e74c3c;
            --warning: #f39c12;
            --success: #27ae60;
        }
        
        .gradient-bg { background: linear-gradient(135deg, #16a085 0%, #1abc9c 50%, #2ecc71 100%); }
        
        .glass-card {
            background: rgba(255, 255, 255, 0.98);
            backdrop-filter: blur(20px);
            border: 1px solid rgba(255, 255, 255, 0.3);
        }
        
        .glass-dark {
            background: rgba(255, 255, 255, 0.15);
            backdrop-filter: blur(20px);
            border: 1px solid rgba(255, 255, 255, 0.2);
        }
        
        .card-shadow { 
            box-shadow: 0 10px 40px rgba(22, 160, 133, 0.15), 0 4px 12px rgba(0,0,0,0.05); 
        }
        
        .float-animation {
            animation: float 3s ease-in-out infinite;
        }
        
        @keyframes float {
            0%, 100% { transform: translateY(0px); }
            50% { transform: translateY(-8px); }
        }
        
        .pulse-alert {
            animation: pulse-alert 1.5s ease-in-out infinite;
        }
        
        @keyframes pulse-alert {
            0%, 100% { transform: scale(1); box-shadow: 0 0 0 0 rgba(231, 76, 60, 0.7); }
            50% { transform: scale(1.02); box-shadow: 0 0 0 10px rgba(231, 76, 60, 0); }
        }
        
        .reminder-card {
            transition: all 0.3s ease;
        }
        
        .reminder-card:hover { 
            transform: translateY(-3px);
            box-shadow: 0 8px 25px rgba(0,0,0,0.1);
        }
        
        .notification-popup {
            animation: slideDown 0.5s cubic-bezier(0.68, -0.55, 0.265, 1.55);
        }
        
        @keyframes slideDown {
            from { transform: translateY(-150%); opacity: 0; }
            to { transform: translateY(0); opacity: 1; }
        }
        
        .big-btn {
            min-height: 60px;
            font-size: 1.1rem;
            transition: all 0.2s ease;
        }
        
        .big-btn:active {
            transform: scale(0.97);
        }
        
        .elder-text { font-size: 1.15rem; }
        .elder-text-lg { font-size: 1.4rem; }
        
        .status-pending { 
            background: linear-gradient(135deg, #fff9e6 0%, #fff3cd 100%);
            border-left: 5px solid #f39c12;
        }
        
        .status-done { 
            background: linear-gradient(135deg, #e8f8f0 0%, #d1f2eb 100%);
            border-left: 5px solid #27ae60;
        }
        
        .status-alert { 
            background: linear-gradient(135deg, #fdeaea 0%, #fadbd8 100%);
            border-left: 5px solid #e74c3c;
        }
        
        .modal-backdrop {
            background: rgba(0, 0, 0, 0.5);
            backdrop-filter: blur(4px);
        }
        
        .time-input {
            font-size: 1.3rem;
            letter-spacing: 2px;
        }
        
        input[type="time"]::-webkit-calendar-picker-indicator {
            filter: invert(40%) sepia(80%) saturate(500%) hue-rotate(120deg);
            cursor: pointer;
            padding: 5px;
        }
        
        .scrollbar-hide::-webkit-scrollbar { display: none; }
        .scrollbar-hide { -ms-overflow-style: none; scrollbar-width: none; }
        
        /* High Contrast Mode */
        .high-contrast .reminder-card {
            border-width: 3px !important;
        }
        .high-contrast .elder-text { font-size: 1.3rem; }
        .high-contrast .elder-text-lg { font-size: 1.6rem; }
        
        .emergency-btn {
            animation: emergency-pulse 2s infinite;
        }
        
        @keyframes emergency-pulse {
            0%, 100% { box-shadow: 0 0 0 0 rgba(231, 76, 60, 0.4); }
            50% { box-shadow: 0 0 0 15px rgba(231, 76, 60, 0); }
        }
        
        /* Install Banner */
        .install-banner {
            animation: slideUp 0.5s ease-out;
        }
        
        @keyframes slideUp {
            from { transform: translateY(100%); }
            to { transform: translateY(0); }
        }
        
        /* Safe area for notched phones */
        .safe-top { padding-top: env(safe-area-inset-top); }
        .safe-bottom { padding-bottom: env(safe-area-inset-bottom); }
    </style>
</head>
<body class="bg-gradient-to-br from-slate-50 via-emerald-50 to-teal-50 min-h-screen safe-bottom" id="app-body">
    
    <!-- Install App Banner -->
    <div id="install-banner" class="hidden fixed bottom-0 left-0 right-0 z-50 p-4 install-banner safe-bottom">
        <div class="bg-gradient-to-r from-teal-600 to-emerald-600 text-white p-4 rounded-2xl shadow-2xl max-w-lg mx-auto">
            <div class="flex items-center gap-4">
                <div class="w-14 h-14 bg-white/20 rounded-xl flex items-center justify-center text-3xl">
                    💊
                </div>
                <div class="flex-1">
                    <p class="font-bold text-lg">Install CareAide App</p>
                    <p class="text-white/80 text-sm">Add to home screen for quick access</p>
                </div>
                <div class="flex gap-2">
                    <button onclick="hideInstallBanner()" class="px-3 py-2 rounded-lg bg-white/20 hover:bg-white/30 transition">
                        Later
                    </button>
                    <button onclick="installApp()" class="px-4 py-2 rounded-lg bg-white text-teal-600 font-bold hover:bg-gray-100 transition">
                        Install
                    </button>
                </div>
            </div>
        </div>
    </div>

    <!-- Notification Popup -->
    <div id="notification" class="hidden fixed top-4 right-4 left-4 md:left-auto md:w-[420px] z-50 notification-popup safe-top">
        <div class="bg-gradient-to-r from-emerald-500 to-teal-500 text-white p-5 rounded-2xl shadow-2xl">
            <div class="flex items-center gap-4">
                <div class="w-16 h-16 bg-white/20 rounded-full flex items-center justify-center">
                    <i class="fas fa-bell text-3xl"></i>
                </div>
                <div class="flex-1">
                    <p class="font-bold text-xl" id="notif-title">Reminder!</p>
                    <p class="text-white/90" id="notif-message">Time to take your medication</p>
                </div>
                <button onclick="hideNotification()" class="w-12 h-12 bg-white/20 rounded-full flex items-center justify-center hover:bg-white/30 transition">
                    <i class="fas fa-times text-xl"></i>
                </button>
            </div>
        </div>
    </div>

    <!-- Header -->
    <header class="gradient-bg text-white py-6 px-4 relative overflow-hidden safe-top">
        <div class="absolute inset-0 overflow-hidden">
            <div class="absolute -top-1/2 -right-1/4 w-96 h-96 bg-white/10 rounded-full blur-3xl"></div>
            <div class="absolute -bottom-1/2 -left-1/4 w-96 h-96 bg-white/10 rounded-full blur-3xl"></div>
        </div>
        
        <div class="max-w-4xl mx-auto relative">
            <div class="flex items-center justify-between mb-4">
                <div class="flex items-center gap-4">
                    <div class="bg-white/20 p-4 rounded-2xl glass-dark float-animation">
                        <i class="fas fa-hand-holding-heart text-4xl"></i>
                    </div>
                    <div>
                        <h1 class="text-3xl md:text-4xl font-bold tracking-tight">CareAide</h1>
                        <p class="text-white/80 text-lg font-medium">Eldercare Reminder App</p>
                    </div>
                </div>
                <div class="text-right glass-dark px-5 py-3 rounded-2xl">
                    <p class="text-white/80 text-sm uppercase tracking-wider" id="current-date"></p>
                    <p class="text-3xl font-bold tracking-tight" id="current-time"></p>
                </div>
            </div>
            
            <!-- Quick Stats -->
            <div class="grid grid-cols-3 gap-3 mt-4">
                <div class="glass-dark rounded-2xl p-4 text-center">
                    <p class="text-4xl font-bold" id="total-pending">0</p>
                    <p class="text-sm text-white/80 mt-1"><i class="fas fa-clock mr-1"></i> Pending</p>
                </div>
                <div class="glass-dark rounded-2xl p-4 text-center">
                    <p class="text-4xl font-bold text-green-200" id="total-done">0</p>
                    <p class="text-sm text-white/80 mt-1"><i class="fas fa-check-circle mr-1"></i> Done</p>
                </div>
                <div class="glass-dark rounded-2xl p-4 text-center">
                    <p class="text-4xl font-bold text-yellow-200" id="next-reminder">--:--</p>
                    <p class="text-sm text-white/80 mt-1"><i class="fas fa-bell mr-1"></i> Next</p>
                </div>
            </div>
            
            <!-- Accessibility Toggle -->
            <div class="flex justify-center gap-3 mt-4 flex-wrap">
                <button onclick="toggleHighContrast()" class="glass-dark px-4 py-2 rounded-xl text-sm flex items-center gap-2 hover:bg-white/20 transition">
                    <i class="fas fa-eye"></i> High Contrast
                </button>
                <button onclick="toggleSound()" id="sound-toggle" class="glass-dark px-4 py-2 rounded-xl text-sm flex items-center gap-2 hover:bg-white/20 transition">
                    <i class="fas fa-volume-up"></i> Sound On
                </button>
                <button onclick="shareApp()" class="glass-dark px-4 py-2 rounded-xl text-sm flex items-center gap-2 hover:bg-white/20 transition">
                    <i class="fas fa-share-alt"></i> Share
                </button>
            </div>
        </div>
    </header>

    <!-- Main Content -->
    <main class="max-w-4xl mx-auto p-4 -mt-2 relative z-10">
        
        <!-- Active Alerts Section -->
        <div id="alerts-section" class="hidden mb-6">
            <div class="bg-gradient-to-r from-red-500 to-rose-500 rounded-2xl p-5 shadow-xl pulse-alert">
                <div class="flex items-center gap-4 text-white mb-4">
                    <div class="w-14 h-14 bg-white/20 rounded-full flex items-center justify-center">
                        <i class="fas fa-exclamation-triangle text-2xl"></i>
                    </div>
                    <div>
                        <h2 class="text-2xl font-bold">🔔 Active Alerts!</h2>
                        <p class="text-white/80">It's time for your reminder</p>
                    </div>
                </div>
                <div id="active-alerts" class="space-y-3">
                    <!-- Active alerts will be inserted here -->
                </div>
            </div>
        </div>

        <!-- Emergency Contact Card -->
        <div class="glass-card rounded-2xl p-4 card-shadow mb-6">
            <div class="flex items-center justify-between">
                <div class="flex items-center gap-3">
                    <div class="w-12 h-12 bg-red-100 rounded-xl flex items-center justify-center">
                        <i class="fas fa-phone-alt text-red-500 text-xl"></i>
                    </div>
                    <div>
                        <p class="font-bold text-gray-800 elder-text">Emergency Contact</p>
                        <p class="text-gray-500" id="emergency-name">Click to set contact</p>
                    </div>
                </div>
                <div class="flex gap-2">
                    <button onclick="callEmergency()" class="emergency-btn w-14 h-14 bg-red-500 hover:bg-red-600 text-white rounded-xl flex items-center justify-center transition shadow-lg">
                        <i class="fas fa-phone text-xl"></i>
                    </button>
                    <button onclick="editEmergencyContact()" class="w-14 h-14 bg-gray-100 hover:bg-gray-200 text-gray-600 rounded-xl flex items-center justify-center transition">
                        <i class="fas fa-edit text-xl"></i>
                    </button>
                </div>
            </div>
        </div>

        <!-- Add Reminder Form -->
        <div class="glass-card rounded-3xl p-6 card-shadow mb-6">
            <div class="flex items-center gap-3 mb-6">
                <div class="w-12 h-12 gradient-bg rounded-xl flex items-center justify-center text-white">
                    <i class="fas fa-plus text-xl"></i>
                </div>
                <h2 class="text-2xl font-bold text-gray-800">Add New Reminder</h2>
            </div>
            
            <form id="reminder-form" class="space-y-5">
                <div>
                    <label class="block text-gray-600 mb-2 font-semibold elder-text">
                        <i class="fas fa-comment-medical mr-2 text-teal-500"></i>Reminder Message
                    </label>
                    <input type="text" id="message" required placeholder="e.g., Take morning medicine, Drink water" 
                        class="w-full px-5 py-4 rounded-xl border-2 border-gray-200 focus:border-teal-500 focus:ring-4 focus:ring-teal-100 outline-none transition text-gray-700 elder-text bg-gray-50">
                </div>
                
                <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
                    <div>
                        <label class="block text-gray-600 mb-2 font-semibold elder-text">
                            <i class="fas fa-clock mr-2 text-teal-500"></i>Time (HH:MM)
                        </label>
                        <input type="time" id="reminder-time" required 
                            class="w-full px-5 py-4 rounded-xl border-2 border-gray-200 focus:border-teal-500 focus:ring-4 focus:ring-teal-100 outline-none transition text-gray-700 time-input bg-gray-50">
                    </div>
                    <div>
                        <label class="block text-gray-600 mb-2 font-semibold elder-text">
                            <i class="fas fa-tag mr-2 text-teal-500"></i>Category
                        </label>
                        <select id="category" 
                            class="w-full px-5 py-4 rounded-xl border-2 border-gray-200 focus:border-teal-500 focus:ring-4 focus:ring-teal-100 outline-none transition text-gray-700 elder-text bg-gray-50">
                            <option value="medication">💊 Medication</option>
                            <option value="water">💧 Drink Water</option>
                            <option value="exercise">🚶 Exercise / Walk</option>
                            <option value="meal">🍽️ Meal Time</option>
                            <option value="appointment">🏥 Doctor Appointment</option>
                            <option value="other">📋 Other</option>
                        </select>
                    </div>
                </div>
                
                <div>
                    <label class="block text-gray-600 mb-2 font-semibold elder-text">
                        <i class="fas fa-redo mr-2 text-teal-500"></i>Repeat
                    </label>
                    <div class="grid grid-cols-3 gap-3">
                        <label class="flex items-center justify-center gap-2 p-3 bg-gray-50 rounded-xl cursor-pointer border-2 border-gray-200 has-[:checked]:border-teal-500 has-[:checked]:bg-teal-50 transition">
                            <input type="radio" name="frequency" value="once" class="hidden">
                            <span class="elder-text font-medium">Once</span>
                        </label>
                        <label class="flex items-center justify-center gap-2 p-3 bg-gray-50 rounded-xl cursor-pointer border-2 border-gray-200 has-[:checked]:border-teal-500 has-[:checked]:bg-teal-50 transition">
                            <input type="radio" name="frequency" value="daily" checked class="hidden">
                            <span class="elder-text font-medium">Daily</span>
                        </label>
                        <label class="flex items-center justify-center gap-2 p-3 bg-gray-50 rounded-xl cursor-pointer border-2 border-gray-200 has-[:checked]:border-teal-500 has-[:checked]:bg-teal-50 transition">
                            <input type="radio" name="frequency" value="weekly" class="hidden">
                            <span class="elder-text font-medium">Weekly</span>
                        </label>
                    </div>
                </div>
                
                <button type="submit" class="w-full gradient-bg text-white py-5 rounded-xl font-bold text-xl hover:opacity-90 transition flex items-center justify-center gap-3 shadow-lg big-btn">
                    <i class="fas fa-plus-circle text-2xl"></i>
                    Add Reminder
                </button>
            </form>
        </div>

        <!-- Quick Add Buttons -->
        <div class="glass-card rounded-2xl p-4 card-shadow mb-6">
            <p class="text-gray-500 font-semibold mb-3 elder-text"><i class="fas fa-bolt mr-2"></i>Quick Add</p>
            <div class="grid grid-cols-2 md:grid-cols-4 gap-3">
                <button onclick="quickAdd('medication', '💊 Take Medicine')" 
                    class="big-btn flex flex-col items-center justify-center gap-2 p-4 bg-gradient-to-r from-rose-500 to-pink-500 text-white rounded-xl shadow-lg active:scale-95 transition">
                    <span class="text-3xl">💊</span>
                    <span class="font-semibold">Medicine</span>
                </button>
                <button onclick="quickAdd('water', '💧 Drink Water')" 
                    class="big-btn flex flex-col items-center justify-center gap-2 p-4 bg-gradient-to-r from-cyan-500 to-blue-500 text-white rounded-xl shadow-lg active:scale-95 transition">
                    <span class="text-3xl">💧</span>
                    <span class="font-semibold">Water</span>
                </button>
                <button onclick="quickAdd('exercise', '🚶 Take a Walk')" 
                    class="big-btn flex flex-col items-center justify-center gap-2 p-4 bg-gradient-to-r from-emerald-500 to-green-500 text-white rounded-xl shadow-lg active:scale-95 transition">
                    <span class="text-3xl">🚶</span>
                    <span class="font-semibold">Walk</span>
                </button>
                <button onclick="quickAdd('meal', '🍽️ Meal Time')" 
                    class="big-btn flex flex-col items-center justify-center gap-2 p-4 bg-gradient-to-r from-amber-500 to-orange-500 text-white rounded-xl shadow-lg active:scale-95 transition">
                    <span class="text-3xl">🍽️</span>
                    <span class="font-semibold">Meal</span>
                </button>
            </div>
        </div>

        <!-- Reminders List -->
        <div class="glass-card rounded-3xl p-6 card-shadow">
            <div class="flex items-center justify-between mb-5">
                <div class="flex items-center gap-3">
                    <div class="w-12 h-12 bg-gradient-to-r from-teal-500 to-emerald-500 rounded-xl flex items-center justify-center text-white">
                        <i class="fas fa-list-check text-xl"></i>
                    </div>
                    <h2 class="text-2xl font-bold text-gray-800">Scheduled Reminders</h2>
                </div>
                <button onclick="clearCompleted()" class="px-4 py-2 rounded-xl elder-text font-medium text-gray-500 hover:text-white hover:bg-red-500 transition flex items-center gap-2 border-2 border-gray-200 hover:border-red-500">
                    <i class="fas fa-trash-alt"></i>
                    <span class="hidden md:inline">Clear Done</span>
                </button>
            </div>
            
            <div id="reminders-list" class="space-y-4">
                <!-- Reminders will be added here dynamically -->
            </div>
            
            <div id="empty-state" class="text-center py-12">
                <div class="w-24 h-24 mx-auto mb-6 bg-gradient-to-r from-teal-100 to-emerald-100 rounded-full flex items-center justify-center">
                    <i class="fas fa-calendar-plus text-4xl text-teal-400"></i>
                </div>
                <h3 class="text-xl font-bold text-gray-700 mb-2">No Reminders Yet</h3>
                <p class="text-gray-400 elder-text">Add your first reminder using the form above!</p>
            </div>
        </div>
    </main>

    <!-- Footer -->
    <footer class="text-center py-8 text-gray-400 mt-8">
        <div class="flex items-center justify-center gap-2 mb-2">
            <i class="fas fa-heart text-red-400"></i>
            <span class="font-medium elder-text">CareAide Eldercare App</span>
        </div>
        <p class="text-sm">Built with ❤️ for your loved ones</p>
        <p class="text-xs mt-2 text-gray-300">v1.0 • Works Offline</p>
    </footer>

    <!-- Emergency Contact Modal -->
    <div id="emergency-modal" class="hidden fixed inset-0 z-50 flex items-center justify-center p-4 modal-backdrop">
        <div class="bg-white rounded-3xl p-6 w-full max-w-md shadow-2xl">
            <div class="flex items-center justify-between mb-6">
                <h3 class="text-xl font-bold text-gray-800">Emergency Contact</h3>
                <button onclick="closeEmergencyModal()" class="w-10 h-10 rounded-full bg-gray-100 hover:bg-gray-200 flex items-center justify-center transition">
                    <i class="fas fa-times text-gray-500"></i>
                </button>
            </div>
            <form id="emergency-form" class="space-y-4">
                <div>
                    <label class="block text-gray-600 mb-2 font-semibold elder-text">Contact Name</label>
                    <input type="text" id="emergency-contact-name" required placeholder="e.g., Dr. Smith, Son John" 
                        class="w-full px-4 py-4 rounded-xl border-2 border-gray-200 focus:border-teal-500 outline-none elder-text">
                </div>
                <div>
                    <label class="block text-gray-600 mb-2 font-semibold elder-text">Phone Number</label>
                    <input type="tel" id="emergency-contact-phone" required placeholder="e.g., +1 234 567 8900" 
                        class="w-full px-4 py-4 rounded-xl border-2 border-gray-200 focus:border-teal-500 outline-none elder-text">
                </div>
                <button type="submit" class="w-full gradient-bg text-white py-4 rounded-xl font-bold elder-text hover:opacity-90 transition">
                    Save Contact
                </button>
            </form>
        </div>
    </div>

    <script>
        // ============ PWA INSTALL HANDLING ============
        let deferredPrompt;
        
        window.addEventListener('beforeinstallprompt', (e) => {
            e.preventDefault();
            deferredPrompt = e;
            // Show install banner after 3 seconds
            setTimeout(() => {
                if (!localStorage.getItem('installBannerDismissed')) {
                    document.getElementById('install-banner').classList.remove('hidden');
                }
            }, 3000);
        });
        
        function installApp() {
            if (deferredPrompt) {
                deferredPrompt.prompt();
                deferredPrompt.userChoice.then((choiceResult) => {
                    if (choiceResult.outcome === 'accepted') {
                        showNotification('App Installed! 🎉', 'CareAide is now on your home screen');
                    }
                    deferredPrompt = null;
                    hideInstallBanner();
                });
            }
        }
        
        function hideInstallBanner() {
            document.getElementById('install-banner').classList.add('hidden');
            localStorage.setItem('installBannerDismissed', 'true');
        }
        
        // Share functionality
        async function shareApp() {
            if (navigator.share) {
                try {
                    await navigator.share({
                        title: 'CareAide - Eldercare Reminder App',
                        text: 'Check out this helpful reminder app for elderly care!',
                        url: window.location.href
                    });
                } catch (err) {
                    console.log('Share cancelled');
                }
            } else {
                // Fallback: copy link
                navigator.clipboard.writeText(window.location.href);
                showNotification('Link Copied! 📋', 'Share this link with others');
            }
        }
        
        // ============ APP LOGIC ============
        
        // Initialize from localStorage
        let reminders = JSON.parse(localStorage.getItem('careAideReminders')) || [];
        let emergencyContact = JSON.parse(localStorage.getItem('emergencyContact')) || null;
        let soundEnabled = localStorage.getItem('soundEnabled') !== 'false';
        let highContrast = localStorage.getItem('highContrast') === 'true';

        // Check if it's a new day and reset completed for daily reminders
        const today = new Date().toDateString();
        if (localStorage.getItem('lastDate') !== today) {
            localStorage.setItem('lastDate', today);
            reminders.forEach(r => {
                if (r.frequency === 'daily') {
                    r.done = false;
                    r.alertShown = false;
                }
            });
            saveReminders();
        }

        // Initialize UI
        if (highContrast) document.getElementById('app-body').classList.add('high-contrast');
        updateSoundButton();
        updateEmergencyDisplay();

        // Category icons
        const categoryIcons = {
            medication: '💊',
            water: '💧',
            exercise: '🚶',
            meal: '🍽️',
            appointment: '🏥',
            other: '📋'
        };

        const categoryColors = {
            medication: 'from-rose-50 to-pink-50 border-rose-200',
            water: 'from-cyan-50 to-blue-50 border-cyan-200',
            exercise: 'from-emerald-50 to-green-50 border-emerald-200',
            meal: 'from-amber-50 to-orange-50 border-amber-200',
            appointment: 'from-violet-50 to-purple-50 border-violet-200',
            other: 'from-gray-50 to-slate-50 border-gray-200'
        };

        // Update time display
        function updateTime() {
            const now = new Date();
            document.getElementById('current-time').textContent = now.toLocaleTimeString('en-US', { hour: '2-digit', minute: '2-digit' });
            document.getElementById('current-date').textContent = now.toLocaleDateString('en-US', { weekday: 'long', month: 'short', day: 'numeric' });
        }
        updateTime();
        setInterval(updateTime, 1000);

        // Get next hour rounded
        function getNextHour() {
            const now = new Date();
            now.setHours(now.getHours() + 1);
            now.setMinutes(0);
            return `${String(now.getHours()).padStart(2, '0')}:00`;
        }

        // Quick add reminder
        function quickAdd(category, name) {
            const time = getNextHour();
            const reminder = {
                id: Date.now().toString(),
                message: name,
                time: time,
                frequency: 'daily',
                category: category,
                done: false,
                alertShown: false,
                createdAt: new Date().toISOString()
            };
            
            reminders.push(reminder);
            saveReminders();
            renderReminders();
            showNotification('Added! ✅', `${name} set for ${formatTime(time)}`);
        }

        // Format time for display
        function formatTime(time) {
            const [hours, minutes] = time.split(':');
            const h = parseInt(hours);
            const ampm = h >= 12 ? 'PM' : 'AM';
            const hour12 = h % 12 || 12;
            return `${hour12}:${minutes} ${ampm}`;
        }

        // Render reminders
        function renderReminders() {
            const list = document.getElementById('reminders-list');
            const emptyState = document.getElementById('empty-state');
            
            if (reminders.length === 0) {
                list.innerHTML = '';
                emptyState.classList.remove('hidden');
            } else {
                emptyState.classList.add('hidden');
                
                // Sort by time, pending first
                const sortedReminders = [...reminders].sort((a, b) => {
                    if (a.done !== b.done) return a.done ? 1 : -1;
                    return a.time.localeCompare(b.time);
                });
                
                list.innerHTML = sortedReminders.map(reminder => `
                    <div class="reminder-card flex flex-col md:flex-row md:items-center gap-4 p-5 rounded-2xl border-2 bg-gradient-to-r ${categoryColors[reminder.category]} ${reminder.done ? 'status-done opacity-70' : 'status-pending'}" data-id="${reminder.id}">
                        <div class="flex items-center gap-4 flex-1">
                            <button onclick="toggleDone('${reminder.id}')" class="w-14 h-14 rounded-xl border-3 ${reminder.done ? 'bg-gradient-to-r from-emerald-500 to-green-500 border-emerald-500 text-white' : 'bg-white border-gray-300 hover:border-teal-500'} flex items-center justify-center transition-all flex-shrink-0 shadow-md">
                                ${reminder.done ? '<i class="fas fa-check text-2xl"></i>' : ''}
                            </button>
                            
                            <div class="text-4xl flex-shrink-0">${categoryIcons[reminder.category]}</div>
                            
                            <div class="flex-1 min-w-0">
                                <h3 class="font-bold text-gray-800 elder-text-lg ${reminder.done ? 'line-through' : ''}">${reminder.message}</h3>
                                <p class="text-gray-500 elder-text capitalize">${reminder.frequency} • ${reminder.done ? '✅ Done' : '⏰ Pending'}</p>
                            </div>
                        </div>
                        
                        <div class="flex items-center gap-3 justify-between md:justify-end">
                            <div class="text-right">
                                <p class="text-2xl font-bold text-teal-600">${formatTime(reminder.time)}</p>
                            </div>
                            
                            <div class="flex gap-2">
                                <button onclick="remindLater('${reminder.id}')" class="w-12 h-12 rounded-xl bg-amber-100 text-amber-600 hover:bg-amber-200 flex items-center justify-center transition shadow active:scale-95" title="Remind Later (+5 min)">
                                    <i class="fas fa-clock text-xl"></i>
                                </button>
                                <button onclick="deleteReminder('${reminder.id}')" class="w-12 h-12 rounded-xl bg-red-100 text-red-600 hover:bg-red-200 flex items-center justify-center transition shadow active:scale-95" title="Delete">
                                    <i class="fas fa-trash text-xl"></i>
                                </button>
                            </div>
                        </div>
                    </div>
                `).join('');
            }
            
            updateStats();
            checkAlerts();
        }

        // Update statistics
        function updateStats() {
            const pending = reminders.filter(r => !r.done).length;
            const done = reminders.filter(r => r.done).length;
            
            document.getElementById('total-pending').textContent = pending;
            document.getElementById('total-done').textContent = done;
            
            // Find next upcoming reminder
            const now = new Date();
            const currentTime = `${String(now.getHours()).padStart(2, '0')}:${String(now.getMinutes()).padStart(2, '0')}`;
            
            const upcomingReminders = reminders
                .filter(r => !r.done && r.time >= currentTime)
                .sort((a, b) => a.time.localeCompare(b.time));
            
            if (upcomingReminders.length > 0) {
                document.getElementById('next-reminder').textContent = formatTime(upcomingReminders[0].time);
            } else {
                document.getElementById('next-reminder').textContent = '--:--';
            }
        }

        // Check for active alerts
        function checkAlerts() {
            const now = new Date();
            const currentTime = `${String(now.getHours()).padStart(2, '0')}:${String(now.getMinutes()).padStart(2, '0')}`;
            
            const activeAlerts = reminders.filter(r => !r.done && r.time === currentTime && !r.alertShown);
            const alertsSection = document.getElementById('alerts-section');
            const alertsContainer = document.getElementById('active-alerts');
            
            if (activeAlerts.length > 0) {
                alertsSection.classList.remove('hidden');
                alertsContainer.innerHTML = activeAlerts.map(alert => `
                    <div class="bg-white/90 rounded-xl p-4 flex items-center justify-between">
                        <div class="flex items-center gap-3">
                            <span class="text-3xl">${categoryIcons[alert.category]}</span>
                            <div>
                                <p class="font-bold text-gray-800 elder-text">${alert.message}</p>
                                <p class="text-gray-500">${formatTime(alert.time)}</p>
                            </div>
                        </div>
                        <button onclick="markDoneFromAlert('${alert.id}')" class="big-btn px-6 py-3 bg-green-500 hover:bg-green-600 text-white rounded-xl font-bold flex items-center gap-2 active:scale-95 transition">
                            <i class="fas fa-check"></i> Done
                        </button>
                    </div>
                `).join('');
                
                // Trigger notifications
                activeAlerts.forEach(alert => {
                    if (!alert.alertShown) {
                        alert.alertShown = true;
                        showNotification('⏰ Reminder Time!', alert.message);
                        
                        // Play sound if enabled
                        if (soundEnabled) {
                            playAlertSound();
                        }
                        
                        // Speak the reminder
                        if (soundEnabled && 'speechSynthesis' in window) {
                            const utterance = new SpeechSynthesisUtterance(`Reminder: ${alert.message}`);
                            utterance.rate = 0.9;
                            speechSynthesis.speak(utterance);
                        }
                        
                        // Browser notification
                        if ('Notification' in window && Notification.permission === 'granted') {
                            new Notification('CareAide Reminder ⏰', {
                                body: alert.message,
                                icon: '💊',
                                tag: alert.id,
                                vibrate: [200, 100, 200]
                            });
                        }
                    }
                });
                
                saveReminders();
            } else {
                alertsSection.classList.add('hidden');
            }
            
            // Reset alertShown for reminders that are no longer current
            reminders.forEach(r => {
                if (r.time !== currentTime) {
                    r.alertShown = false;
                }
            });
        }

        // Play alert sound
        function playAlertSound() {
            const audioContext = new (window.AudioContext || window.webkitAudioContext)();
            const oscillator = audioContext.createOscillator();
            const gainNode = audioContext.createGain();
            
            oscillator.connect(gainNode);
            gainNode.connect(audioContext.destination);
            
            oscillator.frequency.value = 800;
            oscillator.type = 'sine';
            gainNode.gain.value = 0.3;
            
            oscillator.start();
            
            setTimeout(() => {
                oscillator.frequency.value = 1000;
            }, 200);
            
            setTimeout(() => {
                oscillator.stop();
            }, 400);
        }

        // Mark done from alert
        function markDoneFromAlert(id) {
            const reminder = reminders.find(r => r.id === id);
            if (reminder) {
                reminder.done = true;
                saveReminders();
                renderReminders();
                showNotification('Great job! 🎉', `${reminder.message} marked as done`);
            }
        }

        // Toggle done status
        function toggleDone(id) {
            const reminder = reminders.find(r => r.id === id);
            if (reminder) {
                reminder.done = !reminder.done;
                saveReminders();
                renderReminders();
                
                if (reminder.done) {
                    showNotification('Well done! ✅', `${reminder.message} completed`);
                }
            }
        }

        // Remind later (5 minutes)
        function remindLater(id) {
            const reminder = reminders.find(r => r.id === id);
            if (reminder) {
                const [hours, minutes] = reminder.time.split(':');
                let newMinutes = parseInt(minutes) + 5;
                let newHours = parseInt(hours);
                
                if (newMinutes >= 60) {
                    newMinutes -= 60;
                    newHours = (newHours + 1) % 24;
                }
                
                reminder.time = `${String(newHours).padStart(2, '0')}:${String(newMinutes).padStart(2, '0')}`;
                reminder.alertShown = false;
                saveReminders();
                renderReminders();
                
                showNotification('Snoozed! 🔁', `Reminder moved to ${formatTime(reminder.time)}`);
            }
        }

        // Delete reminder
        function deleteReminder(id) {
            const reminder = reminders.find(r => r.id === id);
            if (confirm(`Delete "${reminder?.message}"?`)) {
                reminders = reminders.filter(r => r.id !== id);
                saveReminders();
                renderReminders();
            }
        }

        // Clear completed
        function clearCompleted() {
            const completedCount = reminders.filter(r => r.done).length;
            if (completedCount === 0) {
                showNotification('Nothing to clear', 'No completed reminders');
                return;
            }
            
            if (confirm(`Clear ${completedCount} completed reminder(s)?`)) {
                reminders = reminders.filter(r => !r.done);
                saveReminders();
                renderReminders();
            }
        }

        // Add reminder form
        document.getElementById('reminder-form').addEventListener('submit', function(e) {
            e.preventDefault();
            
            const frequency = document.querySelector('input[name="frequency"]:checked')?.value || 'daily';
            
            const reminder = {
                id: Date.now().toString(),
                message: document.getElementById('message').value,
                time: document.getElementById('reminder-time').value,
                frequency: frequency,
                category: document.getElementById('category').value,
                done: false,
                alertShown: false,
                createdAt: new Date().toISOString()
            };
            
            reminders.push(reminder);
            saveReminders();
            renderReminders();
            
            this.reset();
            document.querySelector('input[name="frequency"][value="daily"]').checked = true;
            
            showNotification('Reminder Added! ✅', `${reminder.message} set for ${formatTime(reminder.time)}`);
        });

        // Save to localStorage
        function saveReminders() {
            localStorage.setItem('careAideReminders', JSON.stringify(reminders));
        }

        // Show notification
        function showNotification(title, message) {
            const notif = document.getElementById('notification');
            document.getElementById('notif-title').textContent = title;
            document.getElementById('notif-message').textContent = message;
            notif.classList.remove('hidden');
            
            setTimeout(hideNotification, 4000);
        }

        function hideNotification() {
            document.getElementById('notification').classList.add('hidden');
        }

        // Toggle high contrast
        function toggleHighContrast() {
            highContrast = !highContrast;
            document.getElementById('app-body').classList.toggle('high-contrast');
            localStorage.setItem('highContrast', highContrast);
            showNotification('Display Updated', highContrast ? 'High contrast enabled' : 'Normal display');
        }

        // Toggle sound
        function toggleSound() {
            soundEnabled = !soundEnabled;
            localStorage.setItem('soundEnabled', soundEnabled);
            updateSoundButton();
        }

        function updateSoundButton() {
            const btn = document.getElementById('sound-toggle');
            if (soundEnabled) {
                btn.innerHTML = '<i class="fas fa-volume-up"></i> Sound On';
            } else {
                btn.innerHTML = '<i class="fas fa-volume-mute"></i> Sound Off';
            }
        }

        // Emergency contact functions
        function updateEmergencyDisplay() {
            const nameEl = document.getElementById('emergency-name');
            if (emergencyContact) {
                nameEl.textContent = `${emergencyContact.name} • ${emergencyContact.phone}`;
            } else {
                nameEl.textContent = 'Click edit to set contact';
            }
        }

        function editEmergencyContact() {
            if (emergencyContact) {
                document.getElementById('emergency-contact-name').value = emergencyContact.name;
                document.getElementById('emergency-contact-phone').value = emergencyContact.phone;
            }
            document.getElementById('emergency-modal').classList.remove('hidden');
        }

        function closeEmergencyModal() {
            document.getElementById('emergency-modal').classList.add('hidden');
        }

        document.getElementById('emergency-form').addEventListener('submit', function(e) {
            e.preventDefault();
            emergencyContact = {
                name: document.getElementById('emergency-contact-name').value,
                phone: document.getElementById('emergency-contact-phone').value
            };
            localStorage.setItem('emergencyContact', JSON.stringify(emergencyContact));
            updateEmergencyDisplay();
            closeEmergencyModal();
            showNotification('Saved! ✅', 'Emergency contact updated');
        });

        function callEmergency() {
            if (emergencyContact) {
                window.location.href = `tel:${emergencyContact.phone}`;
            } else {
                editEmergencyContact();
            }
        }

        // Request notification permission
        if ('Notification' in window && Notification.permission === 'default') {
            Notification.requestPermission();
        }

        // Check alerts every 10 seconds
        setInterval(checkAlerts, 10000);
        setInterval(updateStats, 30000);

        // Initial render
        renderReminders();
        
        // Register service worker for offline support
        if ('serviceWorker' in navigator) {
            navigator.serviceWorker.register('data:text/javascript,' + encodeURIComponent(`
                self.addEventListener('install', e => self.skipWaiting());
                self.addEventListener('activate', e => e.waitUntil(clients.claim()));
                self.addEventListener('fetch', e => e.respondWith(fetch(e.request).catch(() => caches.match(e.request))));
            `)).catch(() => {});
        }
    </script>
</body>
</html>
