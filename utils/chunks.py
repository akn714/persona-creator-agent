import tiktoken

def split_into_token_chunks(comments, max_tokens):
    chunks, current_chunk, current_tokens = [], [], 0

    for comment in comments:
        text = json.dumps(comment)
        tokens = count_tokens(text)
        if current_tokens + tokens > max_tokens:
            chunks.append(current_chunk)
            current_chunk, current_tokens = [], 0
        current_chunk.append(comment)
        current_tokens += tokens

    if current_chunk:
        chunks.append(current_chunk)

    return chunks