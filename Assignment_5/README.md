# Instructions

Enter the phrase `python rls_source.py`. Add the following flags if you want to set something to false.

- `--battery_charged`: Make it so that the battery isn't charged
- `--circuit_closed`: Make it so that the circuit isn't closed
- `--communication_enabled`: Communication is not enabled?
- `--ready_to_launch`: The rocket will not be ready to launch
- `--launch`: The rocket will not launch
    args = parser.parse_args()
    main()