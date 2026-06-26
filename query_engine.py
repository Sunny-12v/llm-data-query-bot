from langchain_openai import ChatOpenAI
from langchain.chains import create_sql_query_chain
from langchain_community.utilities import SQLDatabase
import pandas as pd
import sqlite3

class DataQueryEngine:
    def __init__(self, db_path: str):
        self.db_path = db_path
        self.db = SQLDatabase.from_uri(f"sqlite:///{db_path}")
        self.llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)
        self.chain = create_sql_query_chain(self.llm, self.db)

    def run(self, question: str) -> dict:
        try:
            sql = self.chain.invoke({"question": question})
            sql = sql.strip().strip("```sql").strip("```").strip()
            conn = sqlite3.connect(self.db_path)
            df = pd.read_sql_query(sql, conn)
            conn.close()
            explanation = self._explain(question, sql, df)
            return {"sql": sql, "data": df, "explanation": explanation, "error": None}
        except Exception as e:
            return {"sql": "", "data": None, "explanation": "", "error": str(e)}

    def _explain(self, question, sql, df):
        prompt = f'User asked: "{question}". SQL: {sql}. Result had {len(df)} rows. Summarize in 1-2 sentences.'
        return self.llm.invoke(prompt).content
