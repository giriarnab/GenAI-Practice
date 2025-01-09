# RAG Ollama
This is to create a local RAG application with Ollama model.

- app1.py - It is a simple starter app to connect local Ollama using python.
- rag_app.py - It is a basic RAG app that demonstrate how a model perform with and without RAG.
   - URLs provided :
        - https://docs.oracle.com/cd/F25688_01/oipa_activityprocessing/Content/OIPA%20Activity%20Processing/Shared%20Rules%20Engine.htm
        - https://docs.oracle.com/cd/F25688_01/oipa_activityprocessing/Content/OIPA%20Activity%20Processing/Understanding%20Activities.htm 
   - Question : What are different types of activities in OIPA ?
    - Output without using RAG
      1. Oil and Gas Leasing and Permitting: This involves the process of offering, leasing, and permitting for oil and gas exploration and production on federal and state lands.
      2. Regulatory Compliance: Ensuring that operators comply with regulations related to safety, environmental protection, and resource conservation.
      3. Resource Management: Managing the resources in a sustainable manner, including monitoring production levels, 
         ensuring proper well maintenance, and reclamation of abandoned well sites
      4. Geological and Geophysical Studies: Conducting studies to understand the geology and geophysics of the areas 
         under jurisdiction, which helps in identifying potential oil and gas reserves.
      5. Research and Development: Carrying out research on new technologies, methods, and practices for efficient exploration, production, and conservation of oil and gas resources.
      6. Public Engagement: Engaging with the public, stakeholders, and local communities to gather feedback, address concerns, and promote transparency in decision-making processes.
      7. Policy Development: Developing policies and regulations that guide the activities of the organization, taking into account economic, environmental, and social factors.
      8. Inspections and Enforcement: Conducting inspections to ensure compliance with regulations, and enforcing penalties for non-compliance.
      9. Data Management: Collecting, analyzing, and managing data related to oil and gas activities, including production levels, environmental impact, and safety records.
      10. Emergency Response: Preparing for and responding to emergencies such as oil spills, fires, or accidents, ensuring the protection of human health and the environment.
      11. Training and Capacity Building: Providing training and capacity building for staff members and stakeholders to improve their knowledge and skills in various aspects of oil and 
          gas operations.
      12. Collaboration and Coordination: Working with other government agencies, industry partners, and non-governmental organizations to coordinate efforts and share resources in the 
          management of oil and gas resources.
     - Output using RAG
       1. Undo/Reversal Activity: This activity is already processed and it needs to be undone. It is handled by `UndoP1. Undo/Reversal Activity: This activity is already processed and it            needs to be undone. It is handled by `UndoProcessorBll.java`.
       2. Nuv Pending/Gain Loss Pending Activity: This activity is processed and is in active status, but some NUV's are missing or Gain Loss calculation is missing due to missing data. It 
         is handled by `NuvPendingPolicyFinancialProcessorBll.java`.
       3. Policy Level Activity: This activity impacts the policy holder that impacts the policy alone. It is handled by `PolicyFinancialProcessorBll.java`.
       4. Client Level Activity: This activity impacts client data and might impact all policies the client holds. It is handled By `ClientFinancialProcessorBll.java`.
       5. Plan Level Activity: This activity aggregates all policies in the plan like reports or other changes to the plan. It is handled by `PlanFinancialProcessorBll.java`.
       6. Document Generation: Activities that generate only reports are handled by `DocumentProcessorBll` classes. Separate classes exist for Policy Level 
          Documents(`PolicyDocumentProcessorBll`), Plan level documents (`PlanDocumentProcessorBll`), and Client level Documents (`ClientDocumentProcessorBll`).
- rag_app_ui.py - It is a Ollama RAG app with UI.
  - By Default UI will run in http://127.0.0.1:7860/

## Infrasctuctures
- GenAI Model - Ollama
- Embeddings - OllamaEmbeddings
- Vector Database - Chroma
- User Interface - Gradio

## Installations/Dependencies
1. Ollama
2. Python
3. OpenAI
4. Chroma
5. Visual C++
   - https://stackoverflow.com/questions/64261546/how-to-solve-error-microsoft-visual-c-14-0-or-greater-is-required-when-inst
7. Gradio
8. bs4

Reference Video :
https://www.youtube.com/watch?v=jENqvjpkwmw&t=190s

