from utils.model_loader import ModelLoader
from prompt_library.prompt import SYSTEM_PROMPT
from langgraph import StateGraph, MessageState, END, START
from langgraph.prebuilt import ToolNode, tools_codition



class GraphBuilder:
    
    def __init__(self):
        self.tools=[
            # WeatherInfoTool(),
            # PlacesInfoTool(),
            # CalculatorTool(),
            # CurrencyConverterTool()
        ]
        self.system_prompt = SYSTEM_PROMPT
    def agent_function(self,state: MessageState):
        """Main agent function""""
        user_question = state["message"]
        input_question = [self.system_prompt] + user_question
        response = self.llm_with_tools.invoke(input_question)
        return {"message": [response]}
    
    
    def build_graph(self):
        graph_builder=StateGraph(MessageState)
        graph_builder.add_node("agent", self.agent_function)
        graph_builder.add_node("tools", ToolNode(tools=self.tools))
        graph_builder.add_edge(START, "agent")
        graph_builder.add_codition_edge("agent",tools_codition) 
        graph_builder.add_edge("tools", "agents")
        graph_builder.add_edge("agent", END)
        self.graph = graph_builder.compile()
        return self.graph
    
    
    def __call__(self):
        return self.build_graph()
     
    
    
    
    
    