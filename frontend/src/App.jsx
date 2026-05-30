import { useState } from "react";
import axios from "axios";

function App() {

  const [apiName, setApiName] = useState("");
  const [errorMessage, setErrorMessage] = useState("");
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);

  const analyzeError = async () => {

    if (!apiName || !errorMessage) {
      alert("Please fill all fields");
      return;
    }

    try {

      setLoading(true);

      const response = await axios.post(
        "https://ai-api-debugger-backend.onrender.com/analyze",
        {
          api_name: apiName,
          error_message: errorMessage,
        }
      );

      setResult(response.data);

    } catch (error) {

      console.error(error);
      alert("Failed to analyze error");

    } finally {

      setLoading(false);

    }
  };

  return (
    <div className="min-h-screen bg-gray-950 text-white p-8">

      <div className="max-w-5xl mx-auto">

        <h1 className="text-5xl font-bold mb-3">
          AI API Failure Debugger
        </h1>

        <p className="text-gray-400 mb-10">
          Analyze API failures, detect root causes, and generate AI-powered debugging insights.
        </p>

        <div className="bg-gray-900 p-6 rounded-2xl border border-gray-800 shadow-lg">

          <div className="mb-5">

            <label className="block mb-2 text-sm text-gray-300">
              API Name
            </label>

            <input
              type="text"
              placeholder="OpenAI, Stripe, Gemini..."
              value={apiName}
              onChange={(e) => setApiName(e.target.value)}
              className="w-full p-3 rounded-xl bg-gray-800 border border-gray-700 focus:outline-none"
            />

          </div>

          <div className="mb-5">

            <label className="block mb-2 text-sm text-gray-300">
              Error Message
            </label>

            <textarea
              rows="7"
              placeholder="Paste API error message here..."
              value={errorMessage}
              onChange={(e) => setErrorMessage(e.target.value)}
              className="w-full p-3 rounded-xl bg-gray-800 border border-gray-700 focus:outline-none"
            />

          </div>

          <button
            onClick={analyzeError}
            className="bg-white text-black px-6 py-3 rounded-xl font-semibold hover:opacity-80 transition"
          >
            {loading ? "Analyzing..." : "Analyze Error"}
          </button>

        </div>

        {result && (

          <div className="mt-10 bg-gray-900 border border-gray-800 rounded-2xl p-6 shadow-lg">

            <h2 className="text-3xl font-bold mb-6">
              Analysis Result
            </h2>

            <div className="grid md:grid-cols-2 gap-6">

              <div className="bg-gray-800 p-5 rounded-xl">
                <p className="text-gray-400 text-sm mb-1">
                  Category
                </p>

                <p className="text-xl font-semibold">
                  {result.category}
                </p>
              </div>

              <div className="bg-gray-800 p-5 rounded-xl">
                <p className="text-gray-400 text-sm mb-1">
                  Confidence Score
                </p>

                <p className="text-xl font-semibold">
                  {result.confidence_score}
                </p>
              </div>

            </div>

            <div className="bg-gray-800 p-5 rounded-xl mt-6">

              <p className="text-gray-400 text-sm mb-2">
                Root Cause
              </p>

              <p>
                {result.cause}
              </p>

            </div>

            <div className="bg-gray-800 p-5 rounded-xl mt-6">

              <p className="text-gray-400 text-sm mb-2">
                AI Explanation
              </p>

              <p className="leading-7 whitespace-pre-line">
                {result.ai_explanation}
              </p>

            </div>

            <div className="bg-gray-800 p-5 rounded-xl mt-6">

              <p className="text-gray-400 text-sm mb-3">
                Suggested Solutions
              </p>

              <ul className="list-disc ml-5 space-y-2">

                {result.solutions.map((solution, index) => (
                  <li key={index}>
                    {solution}
                  </li>
                ))}

              </ul>

            </div>

          </div>

        )}

      </div>

    </div>
  );
}

export default App;