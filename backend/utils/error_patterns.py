ERROR_PATTERNS = [
    {
        "category": "Rate Limiting",
        "keywords": [
            "429",
            "too many requests",
            "rate limit",
            "quota exceeded"
        ],
        "cause": "Too many requests in short time",
        "solutions": [
            "Use retry logic",
            "Reduce request frequency",
            "Add exponential backoff"
        ]
    },

    {
        "category": "Authentication Error",
        "keywords": [
            "401",
            "unauthorized",
            "invalid api key",
            "authentication failed"
        ],
        "cause": "Invalid or missing API key",
        "solutions": [
            "Check API key",
            "Verify authorization headers"
        ]
    },

    {
        "category": "Server Error",
        "keywords": [
            "500",
            "internal server error",
            "server crashed"
        ],
        "cause": "Internal server failure",
        "solutions": [
            "Check backend logs",
            "Retry later",
            "Verify server status"
        ]
    },

    {
        "category": "Timeout Error",
        "keywords": [
            "timeout",
            "request timed out",
            "gateway timeout"
        ],
        "cause": "Request took too long",
        "solutions": [
            "Increase timeout limit",
            "Optimize API response time"
        ]
    }
]