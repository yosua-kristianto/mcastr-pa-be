INSERT INTO mlops_tbl_model_log (uuid, version_id, user_session_id, prompt, model_output, feedback_actual_output, created_at)
VALUES
(UUID(), 'emotion-analysis-v1', 'session_1', 'What is the emotion?', FLOOR(RAND()*6), FLOOR(RAND()*6), NOW()),
(UUID(), 'emotion-analysis-v1', 'session_2', 'Analyze sadness', FLOOR(RAND()*6), FLOOR(RAND()*6), NOW()),
(UUID(), 'emotion-analysis-v1', 'session_3', 'Analyze happiness', FLOOR(RAND()*6), FLOOR(RAND()*6), NOW()),
(UUID(), 'emotion-analysis-v1', 'session_4', 'Analyze anger', FLOOR(RAND()*6), FLOOR(RAND()*6), NOW()),
(UUID(), 'emotion-analysis-v1', 'session_5', 'Analyze fear', FLOOR(RAND()*6), FLOOR(RAND()*6), NOW()),
(UUID(), 'emotion-analysis-v1', 'session_6', 'Analyze disgust', FLOOR(RAND()*6), FLOOR(RAND()*6), NOW()),
(UUID(), 'emotion-analysis-v1', 'session_7', 'Analyze surprise', FLOOR(RAND()*6), FLOOR(RAND()*6), NOW()),
(UUID(), 'emotion-analysis-v1', 'session_8', 'Analyze neutral', FLOOR(RAND()*6), FLOOR(RAND()*6), NOW()),
(UUID(), 'emotion-analysis-v1', 'session_9', 'General test prompt', FLOOR(RAND()*6), FLOOR(RAND()*6), NOW()),
(UUID(), 'emotion-analysis-v1', 'session_10', 'Edge case test', FLOOR(RAND()*6), FLOOR(RAND()*6), NOW());