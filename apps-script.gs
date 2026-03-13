// ════════════════════════════════════════════════════════════════════════
//  SPOOKY FITNESS CROSSING — Google Apps Script Backend
//  Paste this entire file into your Google Apps Script editor.
// ════════════════════════════════════════════════════════════════════════
//
//  SETUP (takes about 5 minutes):
//
//  STEP 1 — Create your Google Sheet
//    a) Go to sheets.google.com and create a new spreadsheet
//    b) Rename the first tab/sheet to:  Workouts
//    c) Copy the Sheet ID from the URL:
//       https://docs.google.com/spreadsheets/d/  <-- THIS PART -->  /edit
//    d) Paste it into SHEET_ID below (replace YOUR_SHEET_ID_HERE)
//
//  STEP 2 — Open Apps Script
//    a) In your Google Sheet, click  Extensions > Apps Script
//    b) Delete all the existing code in the editor
//    c) Paste this entire file
//    d) Update SHEET_ID below
//    e) Click  File > Save  (name the project "SpookyFitness" or anything)
//
//  STEP 3 — Deploy as a Web App
//    a) Click  Deploy > New deployment
//    b) Click the gear icon ⚙ next to "Select type" → choose  Web app
//    c) Set:
//         Description:    Spooky Fitness Crossing
//         Execute as:     Me
//         Who has access: Anyone
//    d) Click  Deploy
//    e) Click  Authorize access  and allow the permissions
//    f) Copy the  Web app URL  (looks like: https://script.google.com/macros/s/ABC.../exec)
//
//  STEP 4 — Connect to the HTML app
//    a) Open index.html in a text editor
//    b) Find the line near the bottom that says:
//         const SCRIPT_URL = '';
//    c) Paste your Web App URL between the quotes:
//         const SCRIPT_URL = 'https://script.google.com/macros/s/ABC.../exec';
//    d) Save index.html
//
//  STEP 5 — Host the HTML file (so you can use it on your phone)
//    Option A — GitHub Pages (free, easiest):
//      1. Push index.html to your GitHub repo (already done!)
//      2. In GitHub repo → Settings → Pages → Source: main branch / root
//      3. Visit  https://<your-username>.github.io/<repo-name>/
//      4. Bookmark that URL on your phone's home screen
//
//    Option B — Open as a local file on your computer only:
//      Just double-click index.html in your file browser.
//
// ════════════════════════════════════════════════════════════════════════

// ─── CONFIG ─── (edit this line)
const SHEET_ID   = 'YOUR_SHEET_ID_HERE';   // ← replace with your Sheet ID
const SHEET_NAME = 'Workouts';

// Column header definitions (written automatically on first save)
const COLUMNS = [
  'Timestamp',
  'Date',
  'Miles',
  'Duration (min)',
  'Treadmill Intervals (JSON)',
  'Machine',
  'Focus',
  'Sets Done',
  'Weight (lbs)',
  'Reps',
  'Sets Detail (JSON)',
  'Sauna (min)',
  'Notes',
];

// ════════════════════════════════════════════════════════
//  GET — Return last 20 workouts as JSON
//  Called by the "View Recent Workouts" button
// ════════════════════════════════════════════════════════
function doGet(e) {
  try {
    const sheet = SpreadsheetApp.openById(SHEET_ID).getSheetByName(SHEET_NAME);
    const rows  = sheet.getDataRange().getValues();

    if (rows.length <= 1) {
      return jsonResponse([]);
    }

    const headers = rows[0];
    const data = rows.slice(1)
      .reverse()         // newest first
      .slice(0, 20)
      .map(row => {
        const obj = {};
        headers.forEach((h, i) => { obj[h] = row[i]; });
        return {
          timestamp   : obj['Timestamp'],
          date        : obj['Date'],
          miles       : obj['Miles'],
          duration_min: obj['Duration (min)'],
          intervals   : obj['Treadmill Intervals (JSON)'],
          machine     : obj['Machine'],
          focus       : obj['Focus'],
          sets        : obj['Sets Done'],
          weight_lbs  : obj['Weight (lbs)'],
          reps        : obj['Reps'],
          sets_detail : obj['Sets Detail (JSON)'],
          sauna_min   : obj['Sauna (min)'],
          notes       : obj['Notes'],
        };
      });

    return jsonResponse(data);
  } catch (err) {
    return jsonResponse({ error: err.toString() });
  }
}

// ════════════════════════════════════════════════════════
//  POST — Append a new workout row
//  Called when "Save Workout" is tapped
// ════════════════════════════════════════════════════════
function doPost(e) {
  try {
    const d     = JSON.parse(e.postData.contents);
    const sheet = SpreadsheetApp.openById(SHEET_ID).getSheetByName(SHEET_NAME);

    // Auto-create header row on first save
    if (sheet.getLastRow() === 0) {
      const headerRange = sheet.getRange(1, 1, 1, COLUMNS.length);
      headerRange.setValues([COLUMNS]);
      headerRange
        .setFontWeight('bold')
        .setBackground('#6b3fa0')
        .setFontColor('#ffffff');
      sheet.setFrozenRows(1);
    }

    // Append workout data
    sheet.appendRow([
      new Date(),           // Timestamp (auto)
      d.date          || '',
      d.miles         || 0,
      d.duration_min  || 0,
      d.intervals     || '[]',
      d.machine       || '',
      d.focus         || '',
      d.sets          || 0,
      d.weight_lbs    || 0,
      d.reps          || 0,
      d.sets_detail   || '[]',
      d.sauna_min     || 0,
      d.notes         || '',
    ]);

    return jsonResponse({ success: true });
  } catch (err) {
    return jsonResponse({ success: false, error: err.toString() });
  }
}

// ─── Helper ───
function jsonResponse(data) {
  return ContentService
    .createTextOutput(JSON.stringify(data))
    .setMimeType(ContentService.MimeType.JSON);
}

// ════════════════════════════════════════════════════════
//  OPTIONAL: Run this function manually to test that
//  your Sheet ID and permissions are working correctly.
//  Click the ▶ Run button while this function is selected.
// ════════════════════════════════════════════════════════
function testSetup() {
  const sheet = SpreadsheetApp.openById(SHEET_ID).getSheetByName(SHEET_NAME);
  const msg   = `✅ Connected! Sheet "${SHEET_NAME}" has ${sheet.getLastRow()} rows.`;
  Logger.log(msg);
  SpreadsheetApp.getUi().alert(msg);
}
