user_dic = {
    "twitter_user": {
        "username": "YOUR_TWITTER_USERNAME",
        "password": "YOUR_TWITTER_PASSWORD",
        "email": "YOUR_EMAIL",
        "account_password": "YOUR_EMAIL_PASSWORD"
    }
}

openai_dict = {
    "openAI": {
        "key": "YOUR_OPENAI_API_KEY",
        "llms": ["gpt-4-turbo", "gpt-4o", "gpt-3.5-turbo"],
        "content": "You are an expert assistant specialized in analyzing tweets. Your task is to provide a "
                   "comprehensive analysis based on the given prompt and text. Be detailed and precise in "
                   "your response.",
        "prompts": {
            "tweet": {
                "sentimentAnalysis": "Analiza el sentimiento del siguiente tweet. Proporciona un análisis detallado que"
                                     "incluya lo siguiente: la emoción principal (positiva, negativa o neutral), "
                                     "los elementos específicos del texto que contribuyen a ese sentimiento, "
                                     "y una breve"
                                     "explicación sobre por qué el sentimiento se clasifica de esa manera. Si hay algún"
                                     "matiz o cambio de tono en el tweet, menciónalo también.\n\nTweet: \"\"\"\n{"
                                     "text_tweet}\n\"\"\"\n\nAnálisis de sentimiento:\n1. Emoción principal:\n2. "
                                     "Elementos específicos:\n3. Explicación del sentimiento:\n4. Matices o cambios de "
                                     "tono:",
                "politicalAnalysis": "Analiza el siguiente tweet en el contexto de la política española. Proporciona un"
                                     "análisis político completo que incluya lo siguiente: la ideología subyacente del "
                                     "tweet, los matices presentes en el mensaje, y el partido político español más "
                                     "propenso a apoyar o estar de acuerdo con el contenido del tweet. Explica "
                                     "brevemente"
                                     "por qué se ha clasificado de esa manera.\n\nTweet: \"\"\"\n{"
                                     "text_tweet}\n\"\"\"\n\nAnálisis político:\n1. Ideología subyacente:\n2. Matices "
                                     "del"
                                     "mensaje:\n3. Partido político propenso a apoyar:\n4. Explicación:",
                "supportiveTweet": "Lee el siguiente tweet y redacta un nuevo tweet que exprese apoyo y refuerce el "
                                   "mensaje del tweet original. El nuevo tweet debe ser positivo y estar alineado con "
                                   "el"
                                   "contenido y la intención del original.\n\nTweet original: \"\"\"\n{"
                                   "text_tweet}\n\"\"\"\n\nTweet de apoyo:"
            },
            "notice": {
                "sentimentAnalysisNew": "Analiza el sentimiento del siguiente notica. Proporciona un análisis "
                                        "detallado que"
                                        "incluya lo siguiente: la emoción principal (positiva, negativa o neutral), "
                                        "los elementos específicos del texto que contribuyen a ese sentimiento, "
                                        "y una breve"
                                        "explicación sobre por qué el sentimiento se clasifica de esa manera. Si hay "
                                        "algún"
                                        "matiz o cambio de tono en el noticia, menciónalo también.\n\nnoticia: "
                                        "\"\"\"\n{"
                                        "text_new}\n\"\"\"\n\nAnálisis de sentimiento:\n1. Emoción principal:\n2. "
                                        "Elementos específicos:\n3. Explicación del sentimiento:\n4. Matices o "
                                        "cambios de"
                                        "tono:"
            }
        }
    }
}
