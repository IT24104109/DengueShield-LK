import { BrowserRouter, Routes, Route } from 'react-router-dom'
import NavBar from './components/NavBar.jsx'
import Footer from './components/Footer.jsx'
import Dashboard from './pages/Dashboard.jsx'
import ReportForm from './pages/ReportForm.jsx'
import BrowseReports from './pages/BrowseReports.jsx'
import Prevention from './pages/Prevention.jsx'
import About from './pages/About.jsx'

export default function App() {
  return (
    <BrowserRouter>
      <a className="skip-link" href="#main-content">
        Skip to main content
      </a>
      <NavBar />
      <main id="main-content" className="container" tabIndex={-1}>
        <Routes>
          <Route path="/" element={<Dashboard />} />
          <Route path="/report" element={<ReportForm />} />
          <Route path="/browse" element={<BrowseReports />} />
          <Route path="/prevention" element={<Prevention />} />
          <Route path="/about" element={<About />} />
        </Routes>
      </main>
      <Footer />
    </BrowserRouter>
  )
}
