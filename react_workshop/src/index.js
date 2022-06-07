import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import App from './App';
import reportWebVitals from './reportWebVitals';
import {BrowserRouter, Routes, Route} from 'react-router-dom'
import {
  Account,
  About,
  Genres,
  Submissions,
  CreateGroup,
  BrowseGroups,
  ViewAccount,
  UpgradeAccount,
  CreateGenre,
  CreateSubmission,
  ViewSubmissions
} from './Pages'
import {Dashboard} from './Dashboard'
import Groups from './Groups'
import GroupForm from './GroupForm';
import AddGenreForm from './AddGenreForm'
const hdrConfig = {
  firstname: 'William',
  lastname: 'Hearst'
}

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <BrowserRouter>
        <Routes>
          <Route path="/" element={<Dashboard authorName = {hdrConfig}/>}>
            <Route index element={<Groups />} />
            <Route path="/about" element={<About />} />
            <Route path="/account" element={<Account />} />
            <Route path="/account/view" element={<ViewAccount />} />
            <Route path="/account/upgrade" element={<UpgradeAccount />} />
            <Route path="/genres" element={<Genres />} />
            <Route path="/genres/create" element={<AddGenreForm />} />
            <Route path="/groups" element={<Groups />} />
            <Route path="/groups/create" element={<GroupForm />} />
            <Route path="/groups/browse" element={<BrowseGroups />} />
            <Route path="/submissions" element={<Submissions />} />
            <Route path="/submissions/create" element={<CreateSubmission />} />
            <Route path="/submissions/view" element={<ViewSubmissions />} />
          </Route>
        </Routes>
      <App />
    </BrowserRouter>
  </React.StrictMode>
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
