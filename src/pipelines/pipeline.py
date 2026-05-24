from src.agents.agents import build_search_agent, build_reader_agent, writer_chain, critic_chain



#search the web by search agent and get the results 
def run_research_pipeline(topic : str) -> dict :

    state = {}
    
    # step - 1 
    #search agent working
    print("\n" + "="*50)
    print("agent is working ....")
    print("="*50)

    search_agent = build_search_agent()
    search_results = search_agent.invoke({
        "messages":[(
    "user",
    f"search the web for recent and reliable information on the topic: {topic}"
)]
    })
    state["search_results"] = search_results["messages"][-1].content

    print("\n search result ",state["search_results"])


    # step - 2
    #reader agent take the search results and extract the content from the URLs and return the extracted content

    print("\n" + "="*50)
    print("reader agent is working ....")
    print("="*50)

    reader_agent = build_reader_agent()
    reader_results = reader_agent.invoke({
        "messages":[("user",f"extract the content from the URLs in the search results about {topic},"
                    f"and pick the best URLs and extract the content from them.\n\n"
                    f"search results:\n{state['search_results'][:800]}")]
    })

    state["scraped_content"] = reader_results["messages"][-1].content
    print("\nscraped content: \n", state['scraped_content'])



    # step - 3
    #writer agent takes the search results and the extract the content and write a research report on it and return the report

    print("\n"+" ="*50)
    print("Writer agent is drafting the report ...")
    print("="*50)

    research_combined = (
        f"SEARCH RESULTS : \n {state['search_results']} \n\n"
        f"DETAILED SCRAPED CONTENT : \n {state['scraped_content']}"
    )

    state["report"] = writer_chain.invoke({
        "topic" : topic,
        "research" : research_combined
    })

    print("\n Final Report\n",state['report'])

    
    # step - 4
    #critic agent takes the report and evaluate it and return the score and the feedback
    print("\n"+"="*50)
    print(" Critic agent is evaluating the report ...")
    print("="*50)
    state["critique"] = critic_chain.invoke({
        "report" : state["report"]
    })

    print("\n critic report \n", state['critique'])

    return state