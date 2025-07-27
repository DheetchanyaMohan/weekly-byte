
# 📅 Week 1 of 52 — 🔐 Password Generator

This project marks the **first installment of a 52-week coding challenge** I'm undertaking, where I aim to complete **one small project every weekend**. The goal is to stay consistent with my development skills, learn new tools and techniques, and build a habit of regular creation. I'm intentionally starting with something simple — a password generator — to ease into the discipline and set a sustainable pace for the coming weeks. Over time, the projects will grow in complexity as I push myself to explore new areas and deepen my understanding of full-stack development, design, machine learning, DSA, and problem-solving.


# 🔐 Password Generator

A sleek and responsive password generator built using **HTML**, **Tailwind CSS**, and **Vanilla JavaScript**. Generate secure passwords instantly with options to include uppercase letters, numbers, and symbols. This project was undertaken in order to get familar with Tailwind CSS.

---

## 🚀 Features

- 🔢 Customizable password length
- 🔠 Option to include UPPERCASE letters
- 🔢 Include numbers and symbols
- ✂️ Copy password to clipboard
- 💡 Responsive design using Tailwind
- 🧠 Smooth transitions & clean UI

---

## 📂 Project Structure

📁 password-generator
├── index.html # Main UI with Tailwind styling
├── script.js # Password generation and clipboard logic
├── favicon.png
├── README.md # Project documentation (you're reading it!)
└── screenshot.png UI screenshot

## 🧪 Live Demo

👉 [Try it live on GitHub Pages](https://DheetchanyaMohan.github.io/password-generator/)  

---

## 🛠️ How to Use Locally

1. **Clone this repo:**

   ```bash
   git clone https://github.com/yourusername/password-generator.git
   cd password-generator

2. **Open index.html in your browser.**
    No build tools or frameworks required — just plain HTML, Tailwind via CDN, and JavaScript.

---

### 🎨 Tailwind CSS Utility Class Reference

#### 🌐 General Page Styling
- `bg-orange-50`: Sets a light orange background for the page.
- `text-gray-900`: Applies dark gray color to text.
- `font-poppins`: Uses the "Poppins" font (requires manual import or Tailwind config).
- `antialiased`: Enables smoother font rendering.

#### 📐 Layout and Flexbox
- `flex`: Applies Flexbox layout to the container.
- `flex-col`: Arranges children in a vertical column.
- `md:flex-row`: Switches to horizontal layout on medium (≥768px) screens.
- `min-h-screen`: Ensures the element fills at least the height of the viewport.
- `w-full`: Sets width to 100% of the parent.

#### 🧱 Container Styling
- `justify-center`: Vertically centers child elements in a flex container.
- `items-center`: Horizontally centers items in a flex container.
- `p-10`: Applies padding of 2.5rem on all sides.
- `bg-white`: Applies a white background.
- `shadow-lg`: Adds a large box shadow.
- `space-y-6`: Adds 1.5rem vertical spacing between child elements.
- `max-w-md`: Limits max width to 28rem.

#### 🔢 Input and Label Styling
- `block`: Makes the label span full width.
- `text-xl`: Sets extra-large font size.
- `font-medium`: Applies medium font weight.
- `font-mono`: Uses a monospace font.
- `mb-1`: Adds 0.25rem bottom margin.
- `w-full`: Makes input take full width of parent.
- `px-4 py-2`: Adds horizontal (1rem) and vertical (0.5rem) padding.
- `border border-purple-400`: Adds a 1px purple border.
- `rounded-md`: Rounds corners moderately.
- `focus:outline-none`: Removes the default browser focus ring.
- `focus:ring-2 focus:ring-purple-500`: Adds a purple ring on focus with 2px thickness.

#### ✅ Checkbox Section
- `flex items-center space-x-2`: Horizontally aligns checkbox and label with spacing.
- `accent-purple-600`: Colors the checkbox indicator purple.
- `w-5 h-5`: Sets checkbox width and height to 1.25rem.
- `text-m`: (Likely a typo — should be `text-sm` or `text-base`)
- `font-mono`: Uses a monospace font.

#### 🔘 Generate Button
- `pt-4`: Adds 1rem padding on top.
- `w-full`: Makes the button span full width.
- `bg-orange-500`: Sets the button background to orange.
- `hover:bg-orange-600`: Darkens background on hover.
- `text-xl`: Sets font size to extra-large.
- `text-white`: Sets text color to white.
- `font-semibold`: Applies semi-bold font weight.
- `py-2 px-4`: Adds vertical and horizontal padding.
- `rounded-lg`: Applies large rounded corners.
- `shadow`: Adds base shadow.
- `transition-all duration-200`: Animates all transitions over 200ms.

#### 🟪 Right Column Styling
- `bg-gradient-to-br`: Adds a diagonal background gradient (top-left to bottom-right).
- `from-orange-400 to-purple-700`: Sets gradient colors from orange to purple.
- `text-white`: Makes text white.
- `p-10`: Adds padding on all sides.
- `text-center`: Centers all text horizontally.
- `space-y-4`: Adds spacing between child elements (1rem).

#### 🔓 Password Output Box
- `text-3xl font-semibold`: Large, bold title.
- `text-xl`: Font size for the password output.
- `bg-white text-gray-900`: Light background with dark text.
- `px-6 py-3`: Padding inside the password box.
- `rounded-md`: Medium rounded corners.
- `font-mono`: Monospaced font.
- `break-all`: Wraps long strings if needed.
- `shadow`: Adds base box shadow.
- `max-w-full overflow-auto`: Enables scroll if content overflows.
- `min-h-[3rem]`: Minimum height of 3rem.

#### 📋 Copy Button
- `hidden`: Hides the button initially.
- `bg-white`: White background.
- `text-purple-700`: Purple text.
- `hover:bg-purple-100`: Light purple background on hover.
- `border border-purple-300`: Purple border.
- `font-semibold`: Bold text.
- `px-4 py-2`: Button padding.
- `rounded-md`: Rounded corners.
- `shadow`: Applies a shadow.
- `transition-all duration-200`: Adds transition effects.
- `text-sm`: Small text size.

#### 🟢 Copy Status Text
- `text-sm`: Small font size.
- `text-green-200`: Light green color.
- `h-5`: Fixed height (1.25rem).
