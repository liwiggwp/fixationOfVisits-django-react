import React from 'react'

class Model extends React.Component {
    render() {
        let modelStyle = {
            display: 'block',
            backgroundColor: 'rgba(0,0,0,0.8)',
        }
        return (
            <div className='modal show fade' style={modelStyle}>
                <div className='modal-dialog'>
                    <div className='modal-content'>
                        <div className='modal-header'>
                            <h5 className='modal-title'>{this.props.subject}</h5>
                            <h6 className='modal-title'>{this.props.modul}</h6>
                            <button type='button' className='btn-close' onClick={this.props.hide}></button>
                        </div>
                        <div className='modal-body'>
                           <p>thgrfd</p>
                                {/* <p>{this.props.student}</p> */}
                            
                            
                        </div>
                    </div>
                </div>
            </div>
        )
    }
}

export default Model