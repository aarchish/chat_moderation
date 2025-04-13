graph TD
    Client -->|POST /login| AuthService
    Client -->|POST /comment| CommentService
    CommentService -->|moderateText(text)| ModerationService
    ModerationService -->|flagged_labels| CommentService
    CommentService -->|Save| CommentDB
    Admin -->|GET /comments/flagged| CommentService
