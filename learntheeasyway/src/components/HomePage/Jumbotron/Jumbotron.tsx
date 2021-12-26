import "./Jumbotron.css"
const Jumbotron=()=>{
    return(
            <div className="jumbotron">
                <div className="jumbo jumbotroninformation">
                    <p>Prepare for your Interview question at a time</p>
                    <p>Work through each questions one at a time.</p>
                </div>
                <div className="jumbo jumbotronsubscribe">
                    <p>Start learning now</p>
                    <p>Get the emails for free, starting now, no question asked.</p>
                    <input type="text" />
                    <p>Your email will never be shared.</p>
                    <button className="subscribe_button">
                        Subscribe
                    </button>
                </div>
            </div>
    )
}
export default Jumbotron